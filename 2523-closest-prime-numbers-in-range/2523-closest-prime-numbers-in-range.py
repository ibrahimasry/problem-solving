class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        primes = [True] * (right + 1)
        primes[0] = primes[1] = False
        n1 = 1
        n2 = prev = -1
        
        for i in range(2, right + 1):
            if primes[i]:
                if i >= left:
                    if prev != -1:
                        if n2 - n1 > i - prev or (n2 * n1 < 0):
                            n1 , n2 = prev , i
                    prev = i
                for j in range(i*i, right+1 , i):
                    primes[j] = False
        if n2 * n1 < 0:
            return [-1,-1]
        return [n1,n2]
        