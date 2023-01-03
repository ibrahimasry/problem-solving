class Solution:
    def taskSchedulerII(self, tasks: List[int], space: int) -> int:
        seen = {}
        gap = 0
        for j , v in enumerate(tasks):
            if v in seen:
                newgap = space - ((j+gap - seen[v]) -1)
                if newgap >= 0:
                    gap = newgap + gap
            seen[v] = j + gap
                
        return gap + len(tasks)

                