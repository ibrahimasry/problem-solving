class Solution:
    def numberOfGoodSubsets(self, nums: List[int]) -> int:
        primes = []
        for i in range(2, 31):
            isPrimes = True
            for j in range(2, i):
                if i % j == 0 :
                    isPrimes = False
                    break
            if isPrimes:
                primes.append(i)
                
        counts = Counter(nums)
        nums = list(counts.keys())
        
        @lru_cache(None)
        def dfs(i, mask):
            if i == len(nums):
                return 1
            ans = 0
            ans = dfs(i + 1, mask)
            key = nums[i]
            if key != 1 :
                isPrimeMask = sum(1 << j for j, p in enumerate(primes) if key % p == 0)
                if key % 4 != 0 and key % 9 != 0 and key % 25 != 0 and mask & isPrimeMask == 0 :
                    ans += dfs(i + 1 , mask | isPrimeMask) * counts[key]
            return ans        
        mod = 10 ** 9 + 7
        return ((dfs(0, 0) - 1) * pow(2, counts[1], mod)) % mod