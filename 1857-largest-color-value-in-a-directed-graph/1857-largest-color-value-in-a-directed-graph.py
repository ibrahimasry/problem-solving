class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        
        graph = defaultdict(list)
        indgrees = defaultdict(int)
        n = len(colors)

        dp = [[0] * 26 for _ in range(n)]

        for u, v in edges:
            graph[u].append(v)
            indgrees[v] += 1
        queue = []
        colorsVal = [ord(c) - ord('a') for c in colors]
        for  node in range(n): 
            if node not in indgrees :
                queue.append(node)
                dp[node][colorsVal[node]] = 1
        visited = 0
        while len(queue) > 0:
            curr = queue.pop()
            visited += 1
            for next in graph[curr]:
                indgrees[next] -= 1
                if indgrees[next] == 0 :
                    queue.append(next)
                for n in range(26):
                    dp[next][n] = max(dp[next][n] , dp[curr][n] + (n == colorsVal[next]))
        return -1 if visited < len(colors) else  max(max(curr) for curr in dp)            