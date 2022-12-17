class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        total = 0
        n = len(arr)
        for i , v in enumerate(arr):
            contributation = ((i+1) * (n-i)+1) // 2
            total += contributation* v
        return total