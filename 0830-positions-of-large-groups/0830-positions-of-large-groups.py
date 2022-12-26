class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        count = defaultdict(list)
        s =  s + "-"
        start = 0
        res = []
        for i , (c1, c2) in enumerate(zip(s,s[1:])):
            if c1 != c2:
                if (i - start) + 1 >= 3:
                    res.append([start, i])
                start = i + 1
        return res