class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        prev = -1
        curr = -1
        start = 0
        res = 0
        for i in range(len(fruits)):
            if prev == -1:
                prev = i
            elif curr == -1 and fruits[i] != fruits[prev]:
                curr = i
            if prev != -1 and curr != -1:
                if fruits[i] == fruits[prev]:
                    curr,prev = i,curr
                elif fruits[i] != fruits[prev] and fruits[i] != fruits[curr]:
                    curr,prev = i, curr
                    start = prev
            res = max((i - start) + 1, res)
        return res
                