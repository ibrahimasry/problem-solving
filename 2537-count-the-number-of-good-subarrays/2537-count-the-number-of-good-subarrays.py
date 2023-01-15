class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        
        count = Counter()
        
        prefix = 0
        left = 0
        res = 0
        n = len(nums)
        pairs = 0
        for right in range(len(nums)):
            count[nums[right]] += 1
            if count[nums[right]] > 1:
                pairs += (count[nums[right]] - 1)
            curr = 0
            prev = -1
            while pairs >= k:
                count[nums[left]] -= 1
                if count[nums[left]] >= 1:
                    pairs -= count[nums[left]] 

                if prev == -1:
                    prefix = left
                    prev = 1
                curr = ((left - prefix) + 1) * (n - right)

                left += 1
            res += curr
        return res