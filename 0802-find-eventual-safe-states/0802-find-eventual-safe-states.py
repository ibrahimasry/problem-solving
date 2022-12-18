class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        
        
        seen = [0] * len(graph)
        ans = []
        def dfs(node):
            if seen[node] != 0 :
                return seen[node] == 2
            seen[node] = 1
            for i in graph[node]:
                if seen[i] == 1 or not dfs(i):
                    return False
            seen[node] = 2
            return True

        for i in range(len(graph)):
            if dfs(i):
                ans.append(i)
    
    

                    
        return ans
    