"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []
        res = []
        
        q = [root]
        
        while q :
            res.append([node.val for node in q])
            curr = []
            for i in range(len(q)):
                curr.extend(q[i].children)
            q = curr
        return res