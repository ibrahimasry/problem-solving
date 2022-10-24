class Solution:
    def countSubgraphsForEachDiameter(self, n: int, edges: List[List[int]]) -> List[int]:
        
        graph = defaultdict(list)
        
        for u, v in edges:
            graph[u-1].append(v-1)
            graph[v-1].append(u-1)
        
        
        def getMax(mask):
            if mask & (mask - 1) == 0:
                return 0
            ans = 0
            for i in range(n):
                if mask & (1 << i) == 0 : continue
                queue = deque([i])
                temp = mask
                temp = temp ^ (1 << i)
                d = 0
                while queue:
                    for _ in range(len(queue)):
                        curr = queue.popleft()

                        for nei in graph[curr]:
                            if temp & (1<< nei):
                                queue.append(nei)
                                temp = temp ^ (1<<nei)
                    d += 1
                if temp:
                    return 0
                ans = max(ans, d)
            return ans -1
        ans = [0] * (n -1)
        for mask in range(1<<n):
            d = getMax(mask)
            if d :
                ans[d-1] += 1
        return ans 
        