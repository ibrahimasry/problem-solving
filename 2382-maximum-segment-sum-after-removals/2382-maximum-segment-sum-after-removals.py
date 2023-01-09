class Solution:
    def maximumSegmentSum(self, nums: List[int], q: List[int]) -> List[int]:
        
        
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        def union(x,y):
            r1 = find(x)
            r2 = find(y)
            if r1 != r2:
                parent[r1] = r2
                count[r2] += count[r1]
        n = len(nums)
        parent = [inf] * n
        count = nums[:]
        
        res = [0] * n
        for i in range(n-1,0,-1):
            parent[q[i]] = q[i]
            j = q[i]
            if j > 0 and parent[j-1] != inf:
                union(j-1,j)
            if j < n - 1 and parent[j+1] != inf:
                union(j+1,j)
            res[i-1] = max(res[i],count[find(j)])
        return res