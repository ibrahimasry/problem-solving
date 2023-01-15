class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        
        count = Counter()
        
        prefix = 0
        left = 0
        res = 0
        n = len(nums)
        pairs = 0
        for right in range(len(nums)):
            pairs += (count[nums[right]])
            count[nums[right]] += 1
            left = prefix
            while pairs >= k:
                count[nums[prefix]] -= 1
                pairs -= count[nums[prefix]] 
                prefix += 1

            res +=  (prefix - left) * (n - right)
        return res