from sortedcontainers import SortedList, SortedSet, SortedDict

class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        
        events = []
        maxHeights = SortedList([0])
        for x, y, z in buildings:
            events.append([x,-z])
            events.append([y,z])
        res = []
        for x,h in sorted(events):
            if h < 0:
                maxHeights.add(-h)
            else :
                maxHeights.discard(h)
            curr = maxHeights[-1]
            if not res or res[-1][1] != curr:
                res.append([x,curr])
        return res

                
                