class Solution:
    def minChanges(self, nums: List[int], k: int) -> int:
        
        #get freq of every num in i % k index
        freq = [Counter() for _ in range(k)]
        for i in range(len(nums)):
            freq[i%k][nums[i]] += 1
        totalCountNum = [sum(f.values()) for f in freq]
        dp = [[sys.maxsize] * 1024 for _ in range(k)]

        for i in range(1024):
            dp[-1][i] = totalCountNum[-1] - freq[-1][i]
        for i in range(k-2, -1, -1):
            changeAll = totalCountNum[i] + min(dp[i+1])
            for xor in range(1024):
                best = changeAll
                for curr in freq[i].keys():
                    best = min(best , totalCountNum[i] - freq[i][curr] + dp[i+1][curr ^ xor])
                dp[i][xor] = best
        return dp[0][0]