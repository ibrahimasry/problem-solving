class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        graph = defaultdict(list)
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)

        def dfs(node,p) :
            count = 0
            common = 0
            for nei in graph[node]:
                if nei == p:
                    continue
                c , dist = dfs(nei,node)
                count += c
                common += dist
            
            if (count  or hasApple[node]) :
                if node == 0:
                    return count, common 
                return count + 1 , common + 2 
            return 0 , 0
        return dfs(0,-1)[1]
