class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        minn = nums[:]
        
        for i in range(1,len(nums)):
            minn[i] = min(nums[i], minn[i-1])
        stack = []
        
        for i in range(len(nums)-1,0,-1):
            while stack and stack[-1] <= minn[i]:
                stack.pop()
            if stack and nums[i] > stack[-1]:
                return True
            stack.append(nums[i])
        return False