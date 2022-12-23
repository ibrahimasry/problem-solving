class Solution:
    def friendRequests(self, n: int, restrictions: List[List[int]], requests: List[List[int]]) -> List[bool]:
        arr=list(range(n))
        def union(x,y):
            r1 = find(x)
            r2 = find(y)
            if r1 != r2:
                arr[r1] = r2
            return arr[r1]
        def find(x):
            if arr[x] != x :
                arr[x] = find(arr[x])
            return arr[x]
        res = []
        for u,v in requests:
            p1 , p2 = find(u), find(v)
            valid = True
            if p1 != p2:
                for x,y in restrictions:
                    px,py = find(x),find(y)
                    if set([px,py]) == set([p1,p2]):
                        valid = False
                        break
            res.append(valid)
            if valid:
                arr[p1] = p2
        return res