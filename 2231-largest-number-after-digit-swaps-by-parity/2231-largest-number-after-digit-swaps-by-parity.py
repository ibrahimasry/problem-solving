class Solution:
    def largestInteger(self, num: int) -> int:
        even = deque()
        odd = deque()
        num = str(num)
        for i,n in enumerate(num):
            if int(n) % 2:
                odd.append(i)
            else :
                even.append(i)
        even = sorted(even,key=lambda x : num[x])
        odd = sorted(odd,key=lambda x : num[x])
        res = []
        i = 0
        seenEven = set(even)
        while even and odd:
            if i in seenEven:
                res.append(even.pop())
            else :
                res.append(odd.pop())
            i += 1
        res += even[::-1] + odd[::-1]
        return int(''.join([num[i]  for i in res]))