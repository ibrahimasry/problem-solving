class Solution:
    def countPalindromes(self, s: str) -> int:
        nums = [int(c) for c in s]
        rCount = Counter(nums)
        rPairs = Counter()
        mod = 10 ** 9 + 7
        for x in nums:
            rCount[x] -= 1
            for y, count in rCount.items():
                rPairs[x * 10 + y] += count
        rCount = Counter(nums)
        lCount = Counter()
        lPairs = Counter()
        ans = 0
        
        for x in nums:
            rCount[x] -= 1
            for y, count in rCount.items():
                rPairs[x * 10 + y] -= count
            

            for i in range(10):
                for j in range(10):
                    v = i * 10 + j
                    ans += rPairs[v] * lPairs[v] % mod
            for y , count in lCount.items():
                lPairs[x*10 + y] += count
            lCount[x] += 1
        return ans % mod