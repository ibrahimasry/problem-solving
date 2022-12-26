class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        count = defaultdict(list)
        s =  s + "-"
        start = 0
        res = []
        for i in range(len(s)-1):
            if s[i] != s[i+1]:
                if (i - start) + 1 >= 3:
                    res.append([start, i])
                start = i + 1
        return res