class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        ans = []
        
        def sub(curr,start):
            nonlocal ans
            if len(curr) >= 2:
                ans.append(curr[:])
            seen = set()
            for i in range(start , len(nums)):
                if nums[i] in seen:
                    continue
                if not curr or curr[-1] <= nums[i]:
                    seen.add(nums[i])
                    curr.append(nums[i])
                    sub(curr, i + 1)
                    curr.pop()
        sub([],0)
        return ans