class Solution:
    def rectangleArea(self, rect: List[List[int]]) -> int:
        
        
        def getArea(w):
            preTop = 0
            ans = 0
            for bottom ,top in intervals:
                bottom = max(preTop, bottom)
                if bottom < top:
                    ans += w * (top - bottom)
                    preTop = top
            return ans
        events = []
        
        for x1, y1, x2, y2 in rect:
            events.append((x1, 1, y1, y2))
            events.append((x2, 0, y1,y2))
        intervals = []
        prevX = 0
        ans = 0
        events.sort(key = lambda x: (x[0] , -x[1]))
        for currX, type, bottom , top in events:
            ans += getArea(currX-prevX)
            if type == 1:
                intervals.append((bottom, top))
                intervals.sort()

            elif type == 0:
                intervals.remove((bottom, top))
            prevX = currX
        return ans % (10 ** 9 +7)