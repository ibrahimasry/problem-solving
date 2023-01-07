class Solution:
    def maximumXOR(self, nums: List[int]) -> int:
        res = 0
        odd = 0
        for i in range(32):
            count = 0
            for n in nums:
                if (n >> i) & 1:
                    count += 1
            if count > 0:
                res |= 1 <<i
        return res