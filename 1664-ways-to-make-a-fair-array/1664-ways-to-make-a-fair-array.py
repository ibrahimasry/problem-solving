class Solution:
    def waysToMakeFair(self, nums: List[int]) -> int:
        rightOdd = 0
        rightEven = 0
        leftOdd = 0
        leftEven = 0
        
        for i, n in enumerate(nums):
            if i % 2:
                rightOdd += n
            else :
                rightEven += n
        res = 0
        
        for i, n in enumerate(nums):
            if i % 2:
                if rightOdd - n + leftEven == leftOdd + rightEven:
                    res += 1
                leftOdd += n
                rightOdd -= n
            else:
                if rightEven - n + leftOdd == leftEven + rightOdd:
                    
                    res += 1
                leftEven += n
                rightEven -= n
        return res