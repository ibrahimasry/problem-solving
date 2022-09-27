class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        
        ans = ""
        nums = list(range(1, n+1))
        k -= 1
        for i in range(1, n+1):
            
            count = factorial(n-i)
            index = k // count
            ans += str(nums[index])
            del nums[index]
            k -= count * index
        return ans    
        