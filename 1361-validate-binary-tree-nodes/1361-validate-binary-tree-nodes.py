class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        
        indegrees = [0] * n
        graph = defaultdict(list)
        
        
        for u, v in enumerate(leftChild):
            if v == -1:
                continue
            indegrees[v] += 1
            if indegrees[v] > 1 :
                return False
            if len(graph[u]) == 2:
                return False
                
            graph[u].append(v)
        for u, v in enumerate(rightChild):
            if v == -1:
                continue
            indegrees[v] += 1
            if indegrees[v] > 1 :
                return False
            if len(graph[u]) == 2:
                return False
                
            graph[u].append(v)

            
        root = None
        for i, r in enumerate(indegrees):
            if r == 0:
                if root:
                    return False
                root = i
        queue = deque([root])
        res = [root]

        while queue :
            curr = queue.popleft()
            
            for v in graph[curr]:
                queue.append(v)
                res.append(v)
        return len(res) == n
            