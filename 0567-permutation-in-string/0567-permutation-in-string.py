class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count = Counter()
        origin = Counter(s1)
        seen = set(s1)
        l = 0
        for i in range(len(s2)):
            count[s2[i]] += 1
            if count == origin:
                return True
            if i >= len(s1) - 1:
                count[s2[l]] -= 1
                if count[s2[l]] == 0:
                    del count[s2[l]]
                l += 1
                
        return False