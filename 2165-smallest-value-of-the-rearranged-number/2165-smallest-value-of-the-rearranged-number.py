class Solution:
    def smallestNumber(self, num: int) -> int:
        num = str(num)
        if num[0].isdigit():
            nums = [1,2,3,4,5,6,7,8,9]
            count = Counter(num)
            res = ""
            for i in nums:
                if count[str(i)] > 0:
                    res += str(i) * count[str(i)]
            if count['0'] > 0:
                return int(res[:1] + '0' * count[str(0)] + res[1:])
            return int(res)
        else :
            res = ""
            count = Counter(num)
            for i in range(9,-1,-1):
                if count[str(i)] > 0:
                    res += str(i) * count[str(i)]
            return  -1 *  int(res)