class Solution:
    def canDistribute(self, nums: List[int], quantity: List[int]) -> bool:
        
        
        @lru_cache(None)
        def dp(mask, index):
            if mask == 0:
                return True
            if index == n :
                return False

            
            curr = mask
            while curr > 0:
                if total[curr] <= freq[index]:
                    if dp(mask ^ curr , index + 1):
                        return True
                curr = (curr - 1) & mask
            return dp(mask, index + 1)
        
        freq = list(Counter(nums).values())
        n = len(freq)
        m = len(quantity)
        total = [0] * (1<< m)
        for mask in range(1 << m):
            for j  in range(m):
                if mask & (1 << j) :
                    total[mask] += quantity[j]
        return dp((1 << m) - 1, 0)
        