class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        count = Counter(tasks)
        res = 0
        for v in count.values():
            if v < 2:
                return -1
            if v % 3 == 0:
                
                res += v//3
            else :
                res += (v//3) + 1
        return res