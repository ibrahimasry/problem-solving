class Solution:
    def smallestNumber(self, num: int) -> int:
        num = str(num)
        count = Counter(num)
        res = ""

        if num[0].isdigit():
            for i in range(1,10):
                if count[str(i)] > 0:
                    res += str(i) * count[str(i)]
            if count['0'] > 0:
                return int(res[:1] + '0' * count[str(0)] + res[1:])
            return int(res)
        else :
            for i in range(9,-1,-1):
                if count[str(i)] > 0:
                    res += str(i) * count[str(i)]
            return  -1 *  int(res)