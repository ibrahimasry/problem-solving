# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestNodes(self, root: Optional[TreeNode], queries: List[int]) -> List[List[int]]:
        arr = []
        
        def dfs(root):
            nonlocal arr
            if not root:
                return
            dfs(root.left)
            arr.append(root.val)
            dfs(root.right)
        dfs(root)
        queries = sorted([(val, index) for index, val in enumerate(queries)])
        n = len(queries)
        prev = -1
        ans = [0] * n 
        i = 0
        for num in arr:
            while i < n:
                q , index = queries[i]
                if q < num:
                    i +=1
                    ans[index] = [prev, num]
                elif q == num:
                    ans[index] = [num, num]
                    i +=1
                else :
                    break
            prev = num
        while i < n:
            q , index = queries[i]

            ans[index] = [prev, -1]
            i += 1
        return ans