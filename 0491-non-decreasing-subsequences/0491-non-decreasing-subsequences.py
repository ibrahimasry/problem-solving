class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        ans = set()
        n = len(nums)
        for i in range(n):
            curr = []
            for prev in ans:
                if not prev or prev[-1] <= nums[i]:
                    curr.append(prev[:] + tuple([nums[i]]))
            curr.append(tuple([nums[i]]))
            for sub in curr:
                ans.add(tuple(sub))
        return [curr for curr in ans if len(curr) > 1]