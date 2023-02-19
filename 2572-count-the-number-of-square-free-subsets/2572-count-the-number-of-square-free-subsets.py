class Solution:
    def squareFreeSubsets(self, nums: List[int]) -> int:
        freq = Counter(nums)
        ones = freq[1]
        del freq[1]
        nums = list(freq.keys())
        count = defaultdict(Counter)
        res = -1
        mod = 10 ** 9 + 7
        for n in nums:
            n1 = n
            start = 2
            if n not in count:
                while start * start <= n:
                    while  n % start == 0:
                        count[n1][start] += 1
                        n = n // start
                    start += 1
                if n > 1:
                    count[n1][n] += 1
        temp = []
        for n in nums:
            found = False
            for c in count[n].values():
                if c > 1:
                    found = True
                    break
            if not found:
                temp.append(n)
        nums = temp
        nums.sort()
        for m in range(1 << len(nums)):
            curr = [0] * 32
            found = False
            total = 1
            for i in range(len(nums)):
                if m >> i & 1 == 0: continue
                countn = count[nums[i]]
                total *= freq[nums[i]]
                for j , c in countn.items():
                    curr[j] += c
                    if curr[j] >= 2:
                        found = True
                        break
                if found:
                    break
            if not found:
                res += total
                res %= mod
        t = pow(2,ones,mod) 
        return (( (res * t) % mod ) + t-1) % mod
