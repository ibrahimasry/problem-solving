
class NumArray:
    def __init__(self, nums: List[int]):
        def buildTree(index, start,end):
            tree=self.tree
            if start > end:
                return None
            if start == end:
                tree[index] = nums[start]
                return
            tree = self.tree
            m = (start + end) // 2
            buildTree(index*2  ,start, m)
            buildTree(index*2+1,m+1,end)
            tree[index] = tree[index*2] + tree[index*2 + 1]
        self.tree = [0] * (len(nums) * 4) 
        self.l = len(nums)
        buildTree(1,0,len(nums)-1)

        

    def update(self, pos: int, val: int) -> None:
            def helper(index, start,end, pos, val):
                tree= self.tree
                if start == end:
                    tree[index] = val
                    return
                m = (start + end) // 2
                if pos <= m:
                    helper(index*2, start,m, pos,val)
                else:
                    helper(index*2+1 , m+1, end, pos , val)
                tree[index] = tree[index*2] + tree[index*2+1]
            return helper(1, 0,self.l - 1 ,pos,val)

        

    def sumRange(self, left: int, right: int) -> int:
        def helper(index,l , r , start, end):
            tree = self.tree
            if start > r or end < l:
                return 0
            if start <= l and end >= r:
                return tree[index]
            m = (l+r) // 2
            if start >= m + 1:
                return helper(index*2+1 ,m+1,r, start,end)
            elif end <= m:
                return helper(index*2,l,m,start, end)
            else:
                return helper(index*2,l,m,start, end) + helper(index*2+1 ,m+1,r, start,end)
        return helper(1,0,self.l-1,left,right)

        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)