class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        xor , xor1 , xor2=[0] * 3
        
        for n in nums:
            xor ^= n
        for i in range(1,len(nums)+1):
            xor ^= i
        right = (xor & -xor)
        
        for i in nums:
            if right & i != 0:
                xor2 ^= i
            else:
                xor1 ^= i
        for i in range(1,len(nums)+1):
            if right & i != 0:
                xor2 ^= i
            else:
                xor1 ^= i
        for n in nums:
            if n == xor2:
                return [xor2,xor1]
        return [xor1,xor2]