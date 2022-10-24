class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        
        @lru_cache(None)
        def dp(loc, fuel):
            if fuel < 0:
                return 0
            ans = 0
            if loc == finish:
                ans = 1
            for i, f in enumerate(locations):
                if i != loc:
                    ans += dp(i, fuel - abs(locations[loc] - f))
            return ans
        return dp(start, fuel) % (10**9 +7)