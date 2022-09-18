class Solution:
    def findIntegers(self, n: int) -> int:
        
        
        fib = [0] * 32
        
        fib[0] = 1
        fib[1] = 2
        
        
        for i in range(2, 32):
            fib[i] = fib[i -1] + fib[i-2]
            
            
        k = 31
        
        ans = 0
        prev = 0
        while k >= 0 :
            if ((1 << k) & n) >= 1:
                ans += fib[k]

                if prev == 1 :
                    return ans
                
                prev = 1
                k -= 1
            else :
                prev = 0
                k -= 1
        return ans  + 1
        