from sortedcontainers import SortedList, SortedSet, SortedDict

class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        
        currMax = 0
        
        events = []
        maxHeights = SortedList([0])
        for x, y, z in buildings:
            events.append([x,-z])
            events.append([y,z])

        heapq.heapify(events)
        res = []
        prev = 0
        while events:
            x,h = heapq.heappop(events)
            if h < 0:
                maxHeights.add(-h)
            else :
                maxHeights.discard(h)
            curr=maxHeights[-1]
            if prev != curr:
                res.append([x,curr])
                prev = curr
        return res

                
                