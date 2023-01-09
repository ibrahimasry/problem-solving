class Solution:
    def waysToBuildRooms(self, prevRoom: List[int]) -> int:
        
        graph = defaultdict(list)
        
        for u,v in enumerate(prevRoom):
            graph[v].append(u)
            
        
        def dfs(node):
            count = 0
            ways = 1
            for nei in graph[node]:
                prevWays , prevCount = dfs(nei)
                count += prevCount
                ways *= prevWays * fact[count] * inv[count-prevCount] * inv[prevCount] % mod
            return ways, count + 1
        mod = 10 ** 9 + 7
        l = len(prevRoom) + 4
        fact = [1] * (l+1)
        inv = [1] * (l+1)        
        for i in range(2,l+1):
            fact[i] = i * fact[i-1] % mod
            inv[i]  = pow(fact[i],-1,mod) % mod
        return dfs(0)[0] % mod
