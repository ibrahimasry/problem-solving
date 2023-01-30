class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * n
        ans = 0
        for i in range(n):
            prev = 0
            for j in range(i):
                if nums[j] < nums[i]:
                    prev += 1
                    ans += dp[j]
                else :
                    dp[j] += prev
        return ans