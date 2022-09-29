import sortedcontainers
class Solution:
    def closestRoom(self, rooms: List[List[int]], queries: List[List[int]]) -> List[int]:
        
        rooms.sort(key=lambda x:-x[1])
        queries = [[q[0], q[1], i] for  i, q in enumerate(queries)]
        queries.sort(key=lambda x : -x[1])
        currRooms = sortedcontainers.SortedList()
        ans = [-1] * len(queries)
        
        j = 0
        for id, size, i in queries:
            while j < len(rooms) and rooms[j][1] >= size:
                currRooms.add(rooms[j][0])
                j += 1
            if currRooms:
                index = currRooms.bisect_left(id)

                cand1 = cand2 = sys.maxsize

                if index < len(currRooms):
                    cand2 = currRooms[index]
                if index > 0:
                    cand1= currRooms[index-1]
                if abs(cand1 - id) <= abs(cand2 - id):
                    ans[i] = cand1
                else :
                    ans[i] = cand2
        return ans        
            