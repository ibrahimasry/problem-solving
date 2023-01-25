# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        ans = None
        def dfs(node , p):
            nonlocal ans
            curr = chr(node.val + ord('a'))
            if not node.left and  not node.right:
                if not ans or ans > curr + p:
                    ans = curr + p
            elif node:
                node.left  and dfs(node.left  , curr + p)
                node.right and dfs(node.right , curr + p)
        dfs(root , "")
        return ans            
            