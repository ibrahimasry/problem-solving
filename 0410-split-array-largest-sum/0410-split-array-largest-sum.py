class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def good(m):
            curr = 0
            count = 0
            for i, num in enumerate(nums):
                if num + curr > m:
                    count += 1
                    curr = num
                elif num + curr <= m:
                    curr += num
            return count < k 
        
        l = max(nums)
        r = sum(nums)
        while l < r:
            mid = (l+r) >> 1
            if good(mid):
                r = mid
            else :
                l = mid + 1
        return l