class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def sub(i ,curr):
            if len(curr) > 1:
                ans.append(curr[:])
            seen = set()
            
            for j in range(i,len(nums)):
                if  nums[j] in seen:
                    continue
                if len(curr) == 0 or curr[-1] <= nums[j]:
                    seen.add(nums[j])
                    curr.append(nums[j])
                    sub(j+1,curr)
                    curr.pop()
        sub(0,[])
        return ans