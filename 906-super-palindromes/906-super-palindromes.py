class Solution:
    def superpalindromesInRange(self, left: str, right: str) -> int:
        ans = 0
        l = int(left)
        r = int(right)
        
        for i in range(0, 2):
            isOdd = -1 if i == 1 else 0
            for i in range(1, r):
                s = str(i) + str(i)[-1+isOdd::-1]
                num = int(s) ** 2
                if num > r:
                    break
                if num >= l and str(num) == str(num)[::-1]:
                    ans += 1
        return ans             