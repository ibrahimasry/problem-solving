class Solution:
    def findMinMoves(self, nums: List[int]) -> int:
        total = sum(nums)
        n = len(nums)
        if total % n != 0 :
            return -1
        
        left  = [0] * n
        right = [0] * n
        ans = 0
        avg = total // n
        for i in range(n):
            if i == 0 :
                left[i] = 0
                right[i] = nums[i] - avg
            elif i == n -1:
                right[i] = 0
                left[i] = nums[i] - avg
            else:
                left[i] = -right[i-1]
                right[i] = nums[i] - avg - left[i]
        for i in range(n):
            temp = 0
            if left[i] > 0 :
                temp+=left[i]
            if right[i] > 0:
                temp+=right[i]
            ans = max(ans, temp)
                
        
        return ans