class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        prev = curr = res = start = 0
        for i in range(len(fruits)):
            if fruits[i] == fruits[prev] or fruits[prev] == fruits[curr]:
                curr,prev = i,curr
            elif fruits[i] not in [fruits[prev] , fruits[curr]]:
                curr,prev = i, curr
                start = prev
            res = max((i - start) + 1, res)
        return res
                