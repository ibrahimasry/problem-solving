class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        i = 0
        res = 0
        while coins and i < len(costs):
            if coins >= costs[i]:
                res += 1
                coins -= costs[i]
                i += 1
            else :
                break
        return res