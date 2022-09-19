# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def canMerge(self, trees: List[TreeNode]) -> Optional[TreeNode]:
        
        leaves = set()
        treeDict = dict()
        
        for tree in trees:
            treeDict[tree.val] = tree
            if tree.left:
                leaves.add(tree.left.val)
            if tree.right:
                leaves.add(tree.right.val)
        root = None
        for val, tree in treeDict.items():
            if val not in leaves:
                root = tree 
                break
        if not root :
            return None
        currLeaves = {}
        if root.left :
            currLeaves[root.left.val] = (-sys.maxsize, root.val, root, 0)
        if root.right:
            currLeaves[root.right.val] = (root.val, sys.maxsize, root, 1)
        del treeDict[root.val]
        while treeDict:
            findTree = False
            for val , (low, high, par, leftOrRight) in currLeaves.items():
                if val not in treeDict:
                     continue
                cand = treeDict[val]
                del currLeaves[val]     

                if cand.left:
                    if cand.left.val > low and cand.left.val < high  and cand.left.val not in currLeaves:
                        currLeaves[cand.left.val] = (low, cand.val, cand, 0)
                    else:
                        return None
                if cand.right:
                    if cand.right.val > low and cand.right.val < high and cand.right.val not in currLeaves:
                        currLeaves[cand.right.val] = (cand.val, high, cand, 1)
                        
                    else:
                         return None
                if leftOrRight == 1:
                    par.right = cand
                else:
                    par.left = cand
                findTree = True
                del treeDict[cand.val]
                break
            if findTree == False:
                return None
        return root        
                                                