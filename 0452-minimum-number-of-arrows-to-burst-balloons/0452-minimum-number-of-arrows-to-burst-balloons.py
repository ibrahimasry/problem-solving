class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key= lambda x:x[1])
        
        prev = points[0]
        
        res = 1
        for l, r in points[1:]:
            if l > prev[1]:
                res += 1
                prev = [l, r]
        return res