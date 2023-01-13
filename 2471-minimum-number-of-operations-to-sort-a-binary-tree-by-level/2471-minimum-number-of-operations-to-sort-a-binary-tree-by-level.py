# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        
        
        queue = deque([root])
        ans = 0
        while queue :
            for _ in range(len(queue)):
                curr = queue.popleft()
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            temp = sorted([[c.val,i] for i, c in enumerate(queue)])
            temp = [i for c,i in temp]
            for i in range(len(temp)):
                while temp[i] != i :
                    j = temp[i]
                    temp[i] ,  temp[j] = temp[j] , temp[i]
                    ans += 1
        return ans