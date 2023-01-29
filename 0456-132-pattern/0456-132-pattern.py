class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        minn = list(accumulate(nums,min))
        stack = []
        for i in range(len(nums)-1,0,-1):
            while stack and stack[-1] <= minn[i]: stack.pop()
            if stack and nums[i] > stack[-1]: return True
            if nums[i] > minn[i]:
                stack.append(nums[i])
        return False