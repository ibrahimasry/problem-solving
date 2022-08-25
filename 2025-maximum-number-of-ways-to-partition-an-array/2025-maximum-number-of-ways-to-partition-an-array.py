class Solution:
    def waysToPartition(self, nums: List[int], k: int) -> int:
        
        prefix = list(accumulate(nums))
        right = Counter()
        left = Counter()
        
        
        
        for i in range(1, len(nums)):
            diff = prefix[i-1] - (prefix[-1] - prefix[i-1])
            right[diff] += 1
            
        ans = right[0]
        
        for i in range(0, len(nums)) :
            d = k - nums[i]
            ans = max(right[-d] + left[d], ans)
            currDiff = prefix[i] - (prefix[-1] - prefix[i])

            right[currDiff] -= 1
            left[currDiff]  += 1
        return ans    