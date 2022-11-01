class Solution:
    def minMoves(self, nums: List[int], k: int) -> int:
        
        ids = [i for i, val in enumerate(nums) if val == 1]
        n = len(ids)
        preSum = [0] * (n+1)

        for  i in range(n):
            preSum[i+1] = ids[i] + preSum[i]
            
            
        ans = sys.maxsize
        for i in range(n-k+1):
            curr = preSum[i+ k] - preSum[i + (k+1)//2] - preSum[i + k//2] + preSum[i]
            ans = min(curr, ans)
        ans -=  ((k//2) * ((k+1)//2))

        return ans
        