class Solution:
    def gardenNoAdj(self, n: int, paths: List[List[int]]) -> List[int]:
        def getAvailable(node):
            for i in range(1,5):
                if i not in used[node]:
                    return i
        graph = defaultdict(list)
        
        for u,v in paths:
            graph[u].append(v)
            graph[v].append(u)
        used = [set() for i in range(0,n+1)]
        
        ans = [] 
        
        for i in range(1,n+1):
            ans.append(getAvailable(i))
            for nei in graph[i]:
                used[nei].add(ans[-1])
        return ans