class Solution:
    def minSessions(self, tasks: List[int], sessionTime: int) -> int:
        
        
        
        @lru_cache(None)
        def dp(prev, mask):
            if mask ==  (1 << n) -1:
                return 0
            ans = 100000000
            for i in range(n):
                if mask >> i & 1:
                    continue
                ans = min(ans, 1 + dp(session - tasks[i], mask | (1 << i )))
   
                if prev - tasks[i] >= 0:
                    newMask = (mask | (1 << i))
                    curr = dp(prev - tasks[i], newMask)
                    ans = min(ans, curr )
            return ans
        n = len(tasks)
        session = sessionTime
        return dp(0,0)