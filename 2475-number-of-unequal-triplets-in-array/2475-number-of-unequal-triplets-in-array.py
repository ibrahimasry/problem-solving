class Solution:
    def unequalTriplets(self, nums: List[int]) -> int:
        
        
        count = Counter(nums)
        right = len(nums)
        
        left = 0
        ans = 0
        
        for n , c in count.items():
            right -= count[n]
            ans += left * right * count[n]
            left += count[n]
        return ans