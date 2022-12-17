class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        counter = Counter(nums)
        
        return sum([(n-1) * n // 2 for n in counter.values() if n >= 2])