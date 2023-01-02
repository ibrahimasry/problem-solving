# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isCompleteTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        q = deque()
        last = False
        q.append(root)
        while q :
            curr = q.popleft()
            if curr and last:
                return False
            if curr:
                q.append(curr.left)
                q.append(curr.right)
            else:
                last = True
        return True