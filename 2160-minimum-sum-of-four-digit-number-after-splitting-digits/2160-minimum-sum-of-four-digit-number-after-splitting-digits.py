class Solution:
    def minimumSum(self, num: int) -> int:
        arr = []
        num = sorted(str(num))

        return int(num[0] + num[3]) + int(num[1] + num[2])