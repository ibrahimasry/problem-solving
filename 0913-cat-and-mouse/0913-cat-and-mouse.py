class Solution:
    def catMouseGame(self, graph: List[List[int]]) -> int:
        
        result = defaultdict(int)
        queue = deque()
        def getPreState(m,c,t):
            nodes = []
            if t == 1:
                for nei in graph[c]:
                    if nei == 0:
                        continue
                    nodes.append((m, nei, 2))
            else :
                for nei in graph[m]:
                    nodes.append((nei, c, 1))
            return nodes
        def nextStateFailed(m,c,t):
            if t == 1:
                for nei in graph[m]:
                    if result[(nei,c,2)] != 2:
                        return False
            if t == 2:
                for nei in graph[c]:
                    if nei == 0 :
                        continue
                    if result[(m,nei,1)] != 1:
                        return False
            return True

        for t in range(1,3):
            for node in range(1,len(graph)):
                    queue.append((node, node, t))
                    result[(node, node, t)] = 2
                    
                    
                    queue.append((0, node, t))
                    result[(0, node, t)] = 1
        while queue:
            m,c,t = queue.popleft()
            r = result[(m,c,t)]

            for m1,c1,t1 in getPreState(m,c,t):
                
                r1 = result[(m1,c1,t1)]
                if r1 > 0: 
                    continue
                if r == 3-t:
                    result[(m1,c1,t1)] = r
                    queue.append((m1,c1,t1))
                elif nextStateFailed(m1,c1,t1):
                    result[(m1,c1,t1)] = 3-t1
                    queue.append((m1,c1,t1))
        return result[(1,2,1)]