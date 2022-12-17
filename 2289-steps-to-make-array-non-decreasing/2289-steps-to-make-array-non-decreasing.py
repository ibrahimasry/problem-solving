class Solution:
    def totalSteps(self, nums: List[int]) -> int:
        
        s = []
        res = 0
        for i in range(len(nums)-1,-1,-1):
            curr = 0
            while s and nums[s[-1][0]] < nums[i]:
               
                el, prev =  s.pop()
                curr = max(prev, curr+1)
                res = max(res, curr)

            s.append((i, curr ))
        return res