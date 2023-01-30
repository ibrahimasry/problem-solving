class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack = []
        ans = [-1] * len(nums)
        for i in range(len(nums) * 2):
            curr = i % len(nums)
            while stack and nums[stack[-1]] < nums[curr]:
                ans[stack.pop()] = nums[curr]
            if i < len(nums):
                stack.append(curr)
        return ans