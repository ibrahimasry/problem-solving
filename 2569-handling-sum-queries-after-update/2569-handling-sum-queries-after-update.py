class Solution:
    def handleQuery(self, nums1: List[int], nums2: List[int], queries: List[List[int]]) -> List[int]:
        seg = [0] * (len(nums1) * 4)
        mark = [False] * len(seg)
        def build(start,s,e,t,v):
            if t > e or t < s:
                return 
            if s == e:
                seg[start] += v
                return 
            m = (s+e) // 2
            build(start * 2 , s , m , t,v)
            build((start * 2 + 1) , m+1,e , t,v)
            seg[start] = seg[start*2] + seg[(start*2) + 1]
        def push(start,l,r):
            if mark[start]:
                seg[start] = ((r-l +1) - seg[start])
                if l != r:
                    mark[start*2] = not mark[start*2+1]
                    mark[start*2 + 1] = not mark[start*2+1]
            mark[start] = False
        def update(start,s,e,l,r):
            push(start,s,e)
            if l > e or r < s:
                return 
            if l <= s and r >= e:
                mark[start] = True
                push(start,s,e)
                return 
            m = (s+e) // 2
            update(start * 2 , s , m , l,r)
            update((start * 2 + 1) , m+1,e , l,r)
            seg[start] = seg[start*2] + seg[(start*2) + 1]
        def query(start,s,e,l,r):
            push(start,s,e)
            if l > e or r < s:
                return 0
            if l <= s and r >= e:
                return seg[start]
            m = (s+e) >> 1
            return query(start * 2 , s,m,l,r ) + query((start *  2) + 1,m+1,e,l,r )
        for i , n in enumerate(nums1):
            build(1,0,len(nums1)-1,i,n)
        ans = []
        curr = sum(nums2)
        for i in range(len(queries)):
            if queries[i][0] == 1:
                t,l,r = queries[i]
                update(1,0,len(nums1)-1,l,r)

            elif queries[i][0] == 2:
                t,p,_ = queries[i]
                val = query(1,0,len(nums1)-1,0,len(nums1) - 1)
                curr += val * p
            else :
                ans.append(curr)


        return ans
                
                    
                    