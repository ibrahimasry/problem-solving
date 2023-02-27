"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        n = len(grid)
        def merge(top,left,bottom,right):

            if left ==  right:
                return Node(grid[top][left],True, None,None,None,None)
            mx = right + left >> 1
            my = top + bottom >> 1
            tlTree = merge(top,left,my,mx)
            trTree = merge(top,mx+1,my,right)
            blTree = merge(my+1,left,bottom,mx)
            brTree = merge(my+1,mx+1,bottom,right)
            
            if (tlTree.val == trTree.val == blTree.val == brTree.val) and tlTree.isLeaf and trTree.isLeaf and blTree.isLeaf and brTree.isLeaf:
                return Node(tlTree.val,True,None,None,None,None)
            return Node(1,False, tlTree,trTree,blTree,brTree)

        
        return merge(0,0,n-1,n-1)