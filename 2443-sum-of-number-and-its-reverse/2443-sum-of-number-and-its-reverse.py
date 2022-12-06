class Solution:
    def sumOfNumberAndReverse(self, num: int) -> bool:
        for i in range(num+1):
            
            rx = int(str(i)[::-1])
            if rx + i == num:
                return True
        return False