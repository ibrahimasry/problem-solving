class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        mapped = {node:label for node,label in enumerate(labels)}
        
        ans  = [0]* n
        
        graph = defaultdict(list)
        for u, v in edges:
            graph[v].append(u)
            graph[u].append(v)
        def dfs(node , parent,psub):
            nonlocal ans
            curr = 1
            sub = defaultdict(int)
            sub[mapped[node]] += 1
            for nei in graph[node]:
                if nei == parent:
                    continue
                dfs(nei,node , sub)
            for key in sub:
                psub[key] += sub[key]
            ans[node] = sub[mapped[node]]
            return curr
        dfs(0,-1 , defaultdict(int))
        return ans
        