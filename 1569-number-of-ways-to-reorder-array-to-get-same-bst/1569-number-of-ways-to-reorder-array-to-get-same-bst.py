class Solution:
    def numOfWays(self, nums: List[int]) -> int:
        
        def comb(left, right):
            return fact[right + left] // fact[left] // fact[right]
        def ways(part):
            if len(part) <= 2 :
                return 1
            parent = part[0]
            left = [num for num in part if num < parent]
            right = [num for num in part if num > parent]
            return ways(left) * ways(right) * comb(len(left) , len(right))
        n = len(nums) + 1
        fact = [1] * n
        
        
        for i in range(2, n):
            fact[i] = fact[i-1] * i 
        return (ways(nums)-1) % (10**9 + 7)

        