class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        ans = set()
        n = len(nums)
        for mask in range(1 << n):
            curr = []
            valid = True
            for i in range(n):
                if mask >> i & 1:
                    if not curr or curr[-1] <= nums[i]:
                        curr.append(nums[i])
                    else :
                        valid = False
                        break
            if len(curr) > 1 and valid:
                ans.add(tuple(curr))
        return ans