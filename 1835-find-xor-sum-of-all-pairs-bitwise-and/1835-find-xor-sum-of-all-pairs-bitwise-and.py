class Solution:
    def getXORSum(self, arr1: List[int], arr2: List[int]) -> int:
        
        
        count1 = [0] * 32
        count2 = [0] * 32
        
        for n in arr1:
            for i in range(31,-1,-1):
                count1[i] += 1 if (n & (1 << i )) else 0 
        for n in arr2:
            for i in range(31,-1,-1):
                count2[i] += 1 if (n & (1 << i )) else 0
        ans = 0
        for i in range(0, 32):
            countOnes = count1[i] * count2[i]
            if countOnes % 2 == 1 :
                ans += 1 << i
        return ans       
        
        