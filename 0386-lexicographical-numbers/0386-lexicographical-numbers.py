class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        
        ans = []
        
        
        def dfs(curr, start):
            nonlocal ans
            if int(curr) <= n:
                ans.append(int(curr))
            else :
                return
            for i in range(0,10):
                dfs(curr + str(i),i)
        for i in range(1,10):
            dfs(str(i) , 0)
        return ans