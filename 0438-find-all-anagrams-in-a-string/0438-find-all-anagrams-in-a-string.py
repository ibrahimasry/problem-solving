class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        count = Counter()
        origin = Counter(p)
        l = len(p)
        j = 0
        res = []
        for i in range(len(s)):
            count[s[i]] += 1
            if count == origin:
                res.append((i-l) + 1)
            if i >= l-1:
                count[s[j]] -= 1
                if count[s[j]] == 0:
                    del count[s[j]]
                j+=1
        return res
        