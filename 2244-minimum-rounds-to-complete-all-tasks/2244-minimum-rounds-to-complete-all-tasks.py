class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        count = Counter(tasks)
        res = 0
        for v in count.values():
            if v < 2:
                return -1
            res += (v+2)//3
        return res