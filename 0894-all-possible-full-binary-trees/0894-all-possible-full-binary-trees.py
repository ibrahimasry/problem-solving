# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        @cache
        def dfs(start,end):
            ans = []
            if end - start == 1 :
                return [TreeNode(0)]
            if (end - start) % 2 == 0:
                return []
            for i in range(start,end):
                right = dfs(i+1,end)
                left =  dfs(start, i)
                for r in right:
                    for l in left:
                       ans.append(TreeNode(0,l,r))
            return ans
        return dfs(0,n)