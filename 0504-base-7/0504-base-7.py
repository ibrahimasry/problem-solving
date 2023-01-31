class Solution:
    def convertToBase7(self, num: int) -> str:
        neg = 1
        if num < 0:
            neg = -1
            num *= -1
        def dfs(num):
            if num == 0:
                return 0
            return dfs(num//7) * 10 + (num % 7)
        res = dfs(num) *neg
        return str(res)
            