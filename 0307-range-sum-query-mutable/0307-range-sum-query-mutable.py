class Node:
    def __init__(self, start,end):
        self.start = start
        self.end = end
        self.total = 0
        self.left = None
        self.right = None

class NumArray:
    def __init__(self, nums: List[int]):
        def buildTree(start,end):
            if start > end:
                return None
            if start == end:
                root = Node(start,end)
                root.total = nums[start]
                return root
            m = (start + end) // 2
            root  = Node(start,end)
            root.left  =  buildTree(start, m)
            root.right = buildTree(m+1,end)
            root.total = root.left.total + root.right.total
            return root
        self.tree = buildTree(0,len(nums)-1)

        

    def update(self, pos: int, val: int) -> None:
            def helper(root, pos, val):
                if root.end == root.start:
                    root.total = val
                    return val
                m = (root.start + root.end) // 2
                if pos <= m:
                    helper(root.left, pos,val)
                else:
                    helper(root.right,pos,val)
                root.total = root.left.total + root.right.total
                return root.total
            return helper(self.tree,pos,val)

        

    def sumRange(self, left: int, right: int) -> int:
        def helper(root, start, end):
            if root.end == end and root.start==start:
                return root.total
            m = (root.start + root.end) // 2
            if start >= m + 1:
                return helper(root.right, start,end)
            elif end <= m:
                return helper(root.left,start, end)
            else:
                return helper(root.left,start,m) + helper(root.right, m+1,end)
        return helper(self.tree,left,right)

        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)