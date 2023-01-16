class Solution:
    def maxOutput(self, n: int, edges: List[List[int]], price: List[int]) -> int:
        subtree = Counter()
        res = 0  
        
        graph = defaultdict(list)
        
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        def dfs(node, parent):
            res = 0
            for nei in graph[node]:
                if nei== parent:
                    continue
                res =  max(dfs(nei, node), res)
            
            subtree[node] = res + price[node]
            return subtree[node]
        
        def dfs2(node, parent, cont):
            path1 = path2 = 0
            c1 = c2 = -1
            curr = price[node]

            for child in graph[node]:
                if child == parent: continue
                if subtree[child] > path1:
                    path1 , path2 = subtree[child] , path1
                    c1 = child 
                elif subtree[child]  > path2:
                    path2 = subtree[child] 
            nonlocal res
            res = max(res ,max(cont, path1))
            curr = price[node]
            for child in graph[node]:
                if child == parent:
                    continue
                if child == c1:
                    dfs2(child, node , max(path2 ,cont) + curr)
                else:
                    dfs2(child, node, max(path1 ,cont) + curr)
        dfs(0, -1)
        dfs2(0,-1,0)
        return res