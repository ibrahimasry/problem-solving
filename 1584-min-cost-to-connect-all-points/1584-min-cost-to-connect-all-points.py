class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        parent = list(range(len(points)))       
        def getDist(p1,p2):
            return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        def union(x, y):
            r1 = find(x)
            r2 = find(y)
            if r1 != r2:
                parent[r1] = parent[r2]
                return False
            return True
        lines = []
        for i in range(len(points)):
            for j in range(i+1, len(points)):
                lines.append((getDist(points[i], points[j]), i, j))
        lines.sort()
        ans = 0
        
        for dist , p1, p2 in lines:
            if not union(p1, p2):
                ans += dist
        return ans