class Solution:
    def minimumTimeRequired(self, jobs: List[int], k: int) -> int:
        jobs.sort(reverse=True)
        def backtrack(i, currMax):
            nonlocal ans
            if currMax >= ans:
                return
            if i == n:
                ans = min(currMax, ans)
                return
            timeSet= set()
            
            for m in range(k):
                if w[m] not in timeSet:
                    w[m] += jobs[i]
                    backtrack(i+1, max(currMax, w[m]))
                    w[m] -= jobs[i]
                    timeSet.add(w[m])
        w = [0] * k
        n = len(jobs)
        ans = sys.maxsize
        backtrack(0,0)
        return ans