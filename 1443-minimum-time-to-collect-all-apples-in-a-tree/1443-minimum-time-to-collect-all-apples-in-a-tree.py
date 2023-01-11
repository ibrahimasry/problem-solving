class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        res = 0
        graph = defaultdict(list)
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)

        def dfs(node,p) :
            nonlocal res
            best = 0
            l = 0
            count = 0
            common = 0
            for nei in graph[node]:
                if nei == p:
                    continue
                c , dist = dfs(nei,node)
                count += c
                best += dist 
                common += dist * 2
                l = max(dist,l)
            if node == 0 and count == 1:
                res += common
                return 1,1
            if count >= 2:
                res += common
                return 1 , 1
            if hasApple[node] :
                return (count + 1 , l+1)
            if count > 0:
                return count , l + 1
            return 0 , 0
        dfs(0,-1)
        return res