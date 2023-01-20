class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        ans = set()
        n = len(nums)
        def sub(i,curr):
            if i >= n:
                if len(curr) > 1:
                    ans.add(tuple(curr))
                return
            if not curr or curr[-1] <= nums[i]:
                curr.append(nums[i])
                sub(i+1,curr)
                curr.pop()
            sub(i+1,curr)
        sub(0,[])
        return ans
