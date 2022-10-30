class Solution:
    def findMinMoves(self, nums: List[int]) -> int:
        total = sum(nums)
        n = len(nums)
        if total % n != 0 :
            return -1
        
        moves  = [0] * n
        res = 0
        avg = total / n
        for i in range(n - 1):
            delta = nums[i] - avg
            nums[i+1] += delta
            
            if delta < 0 :
                
                moves[i+1] += -delta
            else :
                moves[i] += delta
            res = max(res, moves[i])
        res = max(res, nums[-1] - avg + moves[-1])
        
        return int(res)