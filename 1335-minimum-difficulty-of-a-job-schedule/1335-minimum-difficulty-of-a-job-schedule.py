class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        n = len(jobDifficulty)
        @lru_cache(None)
        def dfs(index, remain):
            if index == n or remain == 0:
                if index == n and remain == 0:
                    return 0
                else :
                    return sys.maxsize
                
            currMax = 0
            minn = sys.maxsize
            for i in range(index, n):
                currMax  = max(currMax, jobDifficulty[i])
                minn = min(currMax + dfs(i+1, remain - 1), minn)
            return minn
        if n < d:
            return -1
        ans =  dfs(0, d)
        return -1 if ans == sys.maxsize else ans