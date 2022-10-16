class TreeAncestor:

    def __init__(self, n: int, parent: List[int]):
        self.dp = [[-1] * 20 for _ in range(n)]
        for i in range(n):
            self.dp[i][0] = parent[i]
        for i in range(n):
            for j in range(1,20):
                if self.dp[i][j-1] != -1:
                    self.dp[i][j] = self.dp[self.dp[i][j-1]][j-1]
                    
        

    def getKthAncestor(self, node: int, k: int) -> int:
        
        while k > 0 and node != -1:
            j = int(log2(k))

            node = self.dp[node][j]
            k -= (1 << j)
        return node


# Your TreeAncestor object will be instantiated and called as such:
# obj = TreeAncestor(n, parent)
# param_1 = obj.getKthAncestor(node,k)