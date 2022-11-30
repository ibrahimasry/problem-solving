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
            indexes = {}
            temp = [curr.val for curr in queue]
            for i in range(len(queue)):
                indexes[temp[i]] = i

            temp.sort()
            for i in range(len(temp)):
                while i != indexes[temp[i]]:
                    t = indexes[temp[i]]
                    r = temp[t]
                    temp[t] = temp[i]
                    temp[i] = r 
                    ans += 1
        return ans