class Solution:
    def subarrayLCM(self, nums: List[int], k: int) -> int:
        
        ans = 0
        n = len(nums)
        for i in range(n):
            curr = nums[i]
            if curr == k:
                ans += 1
            for j in range(i+1,n):
                curr = lcm(curr, nums[j])
                if curr == k:
                    ans += 1
                if curr > k:
                    break
        return ans