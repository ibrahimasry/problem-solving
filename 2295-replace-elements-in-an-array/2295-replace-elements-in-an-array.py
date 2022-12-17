class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        
        idxToNum = {v:i for i, v in enumerate(nums)}
        
        
        for fr , to in operations:
            nums[idxToNum[fr]] = to
            curr = idxToNum[fr] 
            del idxToNum[fr]
            idxToNum[to] = curr
        return nums
        
        