# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        res = 0
        
        def dfs(root):
            nonlocal res
            if not root :
                return (False, 0)
            l = dfs(root.left)
            r = dfs(root.right)
            if root.val == start:
                res = max(res, max(l[1], r[1]))
                return (True, 0)
            if l[0]:
                summ = sum([l[1], r[1]]) + 1 
                res = max(res, summ)
                return (True, l[1] + 1)
            if r[0]:

                summ = l[1] + r[1] + 1 
                res = max(res, summ)
                return (True, r[1] + 1)
            return (False ,  max(l[1], r[1]) + 1)
        dfs(root)
        return res