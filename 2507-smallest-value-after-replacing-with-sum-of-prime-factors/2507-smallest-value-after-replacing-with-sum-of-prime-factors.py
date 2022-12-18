class Solution:
    def smallestValue(self, n: int) -> int:
        
        primes = set()
        res = 0
        curr = 0
        curr1 = n
        while True:
            i = 2
            
            while n > 1:
                if n % i != 0:
                    i += 1
                else :
                    n /= i
                    curr += i
            if curr == curr1:
                return curr
            else :
                n = curr
                curr1 = curr
                curr = 0