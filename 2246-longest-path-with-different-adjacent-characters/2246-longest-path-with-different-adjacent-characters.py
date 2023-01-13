class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        
        graph = defaultdict(list)
        for u,v in enumerate(parent):
            graph[v].append(u)

            
            
        pairs = {v:c for v,c in enumerate(s)}
        ans=0
        
        def dfs(node, parent):
            
            
            nonlocal ans
            l = 0
            r = 0
            for nei in graph[node]:
                curr = dfs(nei,node)
                if pairs[nei] != pairs[node]:
                    if l  <= curr:
                        l , r = curr , l 
                    elif curr > r:
                        r = curr
            ans = max(l+r+1, max(l+1,ans))
            return l + 1
        dfs(0,-1)
        return ans