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
            if not node:
                return
            if not node.left and  not node.right:
                curr = chr(node.val + ord('a'))

                if ans == None:
                    ans = curr + p 
                elif ans > curr + p:
                    ans = curr + p
            else :
                curr = chr(node.val + ord('a'))
                dfs(node.left  , curr + p)
                dfs(node.right , curr + p)
        dfs(root , "")
        return ans            
            