class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        
        res = 0
        
        n = len(nums)
        left = 1
        right = 1
        start = 0
        end = n -1
        for i in range(n):
            left *= nums[i]
            right *= nums[~i]
            
            j = n - 1 - i
            if left > 0:
                res = max(i - start + 1, res)
            if right > 0:
                res = max(end - j + 1, res)

            if left == 0:
                left = 1
                start = i + 1
            if right == 0:
                end = j - 1
                right = 1
        return res