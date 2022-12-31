# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        
        ans = 0
        
        def dfs(node):
            nonlocal ans
            if not node:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            
            curr = 0
            val = 0
            if node.left:
                if node.left.val == node.val:
                    curr += (left + 1)
                    val = left + 1
            if node.right :
                if node.right.val == node.val:
                    curr += (right + 1)
                    val = max(val,right + 1)
            ans = max(curr, ans)
            
            return val 
        dfs(root)
        return ans
        