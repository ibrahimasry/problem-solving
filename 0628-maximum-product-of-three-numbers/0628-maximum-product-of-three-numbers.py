class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        max1=max2=max3 = -inf
        min1=min2 = inf
        
        for n in nums:
            if n > max1:
                max1,max2,max3=n,max1,max2
            elif n > max2:
                max2,max3= n, max2
            elif n > max3:
                max3=n
            if n < min1:
                min1, min2 = n, min1
            elif n < min2:
                min2 = n
        if min1 != inf and min2 != inf:
            return max(max3*max1*max2, max1*min2*min1)
        return max3*max1*max2
                
        