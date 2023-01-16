class Solution:
    def countOrders(self, n: int) -> int:
        
        
        mod = 10 ** 9 + 7
        
        ans = 1
        
        for i in range(2 ,n+1):
            space = (i * 2) - 1
            total = space * (space + 1) // 2
            ans *= total 
            ans %= mod
        return ans