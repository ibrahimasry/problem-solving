class Solution:
    def taskSchedulerII(self, tasks: List[int], space: int) -> int:
        seen = {}
        gap = 0
        for j , v in enumerate(tasks):
            k = j + gap
            if v in seen:
                if space > ((k - seen[v]) -1) :
                    gap += (space - ((k - seen[v]) -1))
                    k = j + gap
            seen[v] = k
                
        return gap + len(tasks)

                