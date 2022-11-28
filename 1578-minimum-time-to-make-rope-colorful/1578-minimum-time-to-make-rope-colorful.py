class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        
        n = len(colors)
        maxCost = 0
        ans = 0
        
        for i in range(n):
            ans += neededTime[i]

            maxCost = max(maxCost, neededTime[i])
            if  (i == n-1 or colors[i] != colors[i+1]):
                ans -= maxCost
                maxCost = 0
        return ans