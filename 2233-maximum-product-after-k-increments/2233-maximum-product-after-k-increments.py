class Solution:
    def maximumProduct(self, nums: List[int], k: int) -> int:
        
        if len(nums) == 1:
            return nums[0] + k
        mod = (10 ** 9) + 7
        heapq.heapify(nums)
        while k > 0:
            min_num = heappop(nums)
            delta = min(nums[0] + 1 - min_num, k)
            k -= delta
            heappush(nums, min_num + delta)
        return reduce(lambda x,a:x*a %mod,nums) % mod
    