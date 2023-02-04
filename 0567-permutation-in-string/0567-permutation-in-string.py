class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count = Counter(s1)
        seen = set(s1)
        l = 0
        for i in range(len(s2)):
            if s2[i] not in seen :
                while l < i:
                    count[s2[l]] += 1
                    l += 1
                l = i+1
            if s2[i] in seen and count[s2[i]] == 0:
                while count[s2[i]] == 0:
                    count[s2[l]] += 1
                    l +=1
            if s2[i] in seen and count[s2[i]] > 0 :
                count[s2[i]] -= 1
                if count[s2[i]] == 0:
                    del count[s2[i]]
                if len(count) == 0:
                    return True
        return False