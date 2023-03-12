class Solution:
    def findMinimumTime(self, tasks: List[List[int]]) -> int:
        active = [False] * 2001
        
        tasks.sort(key=lambda x:x[1])
        
        for s , e , d in tasks:
            for c in range(s,e+1):
                if active[c]:
                    d -= 1
            while d > 0 and e >= s:
                if active[e] == False:
                    active[e] = True
                    d -= 1
                e -= 1
        return sum(1 for point in active if point)
        