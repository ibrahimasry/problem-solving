class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        
        ans = []
        
        
        def dfs(curr, start):
            nonlocal ans
            if int(curr) <= n:
                ans.append(int(curr))
            for i in range(0,10):
                if curr * 10 + i  <= n:
                    dfs(curr  * 10 + i,i)
        for i in range(1,10):
            dfs(i , 0)
        return ans