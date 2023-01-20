class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        ans = set()
        n = len(nums)
        for mask in range(1 << n):
            curr = []
            for i in range(n):
                if mask >> i & 1:
                    if not curr or curr[-1] <= nums[i]:
                        curr.append(nums[i])
                    else :
                        break
            if len(curr) > 1:
                ans.add(tuple(curr))
        return ans