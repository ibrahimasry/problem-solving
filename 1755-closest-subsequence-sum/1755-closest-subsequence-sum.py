class Solution:
    def minAbsDifference(self, nums: List[int], goal: int) -> int:
        
        def dfs(i, sum, res, nums):
            if i == len(nums):
                res.append(sum)
                return
            dfs(i+1, sum, res, nums)
            dfs(i+1, sum + nums[i], res, nums)
        sum1=[]
        sum2=[]
        dfs(0, 0, sum1, nums[:len(nums)//2])
        dfs(0, 0, sum2, nums[len(nums)//2:])
        sum2.sort()
        ans = sys.maxsize
        for curr in sum1:
            target = goal - curr
            i = bisect_left(sum2, target)
            if i > 0:
                ans = min(ans, abs(target - sum2[i-1]))
            if i < len(sum2):
                ans = min(ans, abs(target-sum2[i]))
        return ans