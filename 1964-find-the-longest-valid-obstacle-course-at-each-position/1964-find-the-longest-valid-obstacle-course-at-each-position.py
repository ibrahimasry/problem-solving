class Solution:
    def longestObstacleCourseAtEachPosition(self, obstacles: List[int]) -> List[int]:
        dp = []
        ans = []
        
        for c in obstacles:
            index = bisect_right(dp, c)
            if index >= len(dp) :
                dp.append(c)
            else :
                dp[index] = c
            ans.append(index + 1)
            
        return ans    