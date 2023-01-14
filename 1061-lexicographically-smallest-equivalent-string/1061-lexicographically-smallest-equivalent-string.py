class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        
        parent = {c:c for c in string.ascii_letters}
        def union(x,y):
            r1 = find(x)
            r2 = find(y)
            
            if r1 < r2:
                parent[r2] = r1
            else :
                parent[r1] = r2
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        
        for c1,c2 in zip(s1,s2):
            union(c1,c2)
            
        ans = []
        
        for c in baseStr:
            ans.append(find(c))
        return ''.join(ans)