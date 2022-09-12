class Solution:
    def maxTaxiEarnings(self, n: int, rides: List[List[int]]) -> int:
        """    
            lru_cache(None)
            def dfs(i) :
                if i == len(rides) :
                    return 0
                ans1 = dfs(i+1)
                nextIndex = bisect_left(rides, [rides[i][1],0, 0])
                s, e, t = rides[i]
                ans2 = e-s+t+ dfs(nextIndex)
                return max(ans1, ans2)
            rides.sort()
            return dfs(0)
            
            //////
            events = []

            for s, e , t in rides :
                events.append((s, 1,  t , e))


            res = 0
            heapq.heapify(events)
            while len(events):
                s, time, earning , e= heapq.heappop(events)

                if time == 1 :
                    heapq.heappush(events, (e , -1 , res + (e-s+earning), s))
                else :
                    res = max(res, earning)

            return res         
         """
        dp = [0] * (n+1)
        rides.sort()
        j = 0
        for i in range(1, n+1) :
            dp[i] = max(dp[i], dp[i-1])
            
            while j < len(rides) and rides[j][0] == i :
                dp[rides[j][1]] = max(dp[rides[j][1]], dp[i] + rides[j][1] - rides[j][0] + rides[j][2])
                j += 1
        return dp[n]        
                
        
        
        
    