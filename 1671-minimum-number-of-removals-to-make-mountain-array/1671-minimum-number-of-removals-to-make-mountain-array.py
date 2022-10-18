class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        
        
        
        def lis(arr):
            dp = []
            seq = []
            for num in arr:
                index = bisect_left(dp, num)
                if index < len(dp):
                    dp[index] = num
                else:
                    dp.append(num)
                seq.append(len(dp))
            return seq
        right = lis(nums[::-1])
        left =  lis(nums)
        
        n = len(nums)
        maxn = 0
        for i in range(1, n-1):
            if right[n-i-1] > 1 and left[i] > 1:
                maxn = max(maxn, right[n-i-1] + left[i] - 1)
        return n - maxn
        