class Solution:
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        
        graph = defaultdict(list)
        ans = 0
        for u, v in roads:
            graph[u].append(v)
            graph[v].append(u)
        def dfs(node, parent):
            nonlocal ans
            count = 0
            for nei in graph[node]:

                if parent == nei: 
                    continue
                curr = dfs(nei, node)
                ans += (curr + seats-1) // seats
                count += curr
            return count + 1
            
        dfs(0, -1)
        return ans
    
        