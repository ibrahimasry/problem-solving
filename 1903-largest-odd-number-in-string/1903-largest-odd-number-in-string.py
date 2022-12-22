class Solution:
    def largestOddNumber(self, num: str) -> str:
        last = -1
        for i , v in enumerate(num):
            if int(v) % 2 == 1 :
                last = i
        if last == -1:
            return ''
        return num[:last+1]