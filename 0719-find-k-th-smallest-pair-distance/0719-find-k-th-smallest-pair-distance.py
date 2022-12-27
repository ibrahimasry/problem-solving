class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        nums.sort()
        
        l = 0
        h = nums[-1] - nums[0]
        
        while l < h:
            m = (l+h)>>1
            count = 0
            left = 0
            for right in range(len(nums)):
                while left < right and nums[right] - nums[left] > m:
                    left += 1
                count += right - left
            if count >= k:
                h = m
            else :
                l = m + 1
        return l
                