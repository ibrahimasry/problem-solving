class Solution:
    def minimumXORSum(self, nums1: List[int], nums2: List[int]) -> int:
        
        @lru_cache(None)
        def dp(i,mask):
            if mask == (1 << n) -1:
                return 0
            if i == n:
                return sys.maxsize
            ans = sys.maxsize
            for j in range(n):
                if( (mask >> j) & 1)== 0:
                    ans = min(ans, (nums1[i] ^ nums2[j]) + dp(i+1, mask | (1 << j)))
            return ans
        n = len(nums1)
        return dp(0,0)