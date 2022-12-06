class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        freq = defaultdict(int)
        
        ans = 0
        
        res = 0
        curr = 0
        for i , c in enumerate(nums):
            freq[c] += 1
            curr += c
            if i < k-1:
                continue
            
            if i - k >= 0:
                freq[nums[i-k]] -= 1
                curr  -= nums[i-k]
                if freq[nums[i-k]] == 0:
                    del freq[nums[i-k]]
            if len(freq) == k:
                res = max(res, curr)

        return res
            