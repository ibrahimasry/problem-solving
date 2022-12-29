class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        ans = set()
        
        def sub(curr,i):
            nonlocal ans
            if i == len(nums):
                if len(curr) >= 2:
                    ans.add(tuple(curr))
                return
            if not curr or curr[-1] <= nums[i]:
                curr.append(nums[i])
                sub(curr, i + 1)
                curr.pop()
            sub(curr, i + 1)
        sub([],0)
        return ans