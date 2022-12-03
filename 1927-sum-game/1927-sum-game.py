class Solution:
    def sumGame(self, num: str) -> bool:
        
        diff = count = 0
        n = len(num)
        for i, c in enumerate(num):
            if i  < n // 2:
                if c == "?":
                    count += 1
                else :
                    diff += int(c)
            else :
                if c == "?":
                    count -= 1
                else :
                    diff -= int(c)
        if count * diff > 0  :
            return True
        if  count== 0 and diff == 0  :
            return False
        if count == 0:
            return True
        if abs(count) % 2  or abs(diff) < 9:
            return True
        if (abs(count)//2) * 9 < abs(diff) or abs(count//2) * 9 > abs(diff):
            return True
        return False