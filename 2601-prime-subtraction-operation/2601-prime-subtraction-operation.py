class Solution:
    def primeSubOperation(self, nums: List[int]) -> bool:
        primes = [True] * 1001  * 4
        primes[0] = False
        primes[1] = False
        for i in range(2,1001):
            
            if primes[i]:
                for j in range(i+i, 1001, i):
                    primes[j] = False
        arr = [nums[-1]]
        primes = [i for i, n in enumerate(primes) if n]
        for n in nums[::-1][1::]:
            if n >= arr[-1]:
                index = bisect_left(primes,  (n-arr[-1])+1)
                if  n - primes[index] >= arr[-1] or n <= primes[index]:
                    return False
                arr.append(n - primes[index])
            else :
                arr.append(n)
        return True