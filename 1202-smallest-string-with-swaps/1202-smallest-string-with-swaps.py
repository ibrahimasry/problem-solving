class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        parent = list(range(len(s)))       
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        def union(x, y):
            r1 = find(x)
            r2 = find(y)
            if r1 != r2:
                parent[r1] = parent[r2]
        for x, y in pairs:
            union(x,y)
        hash = defaultdict(list)
        for i in range(len(s)):
            hash[find(i)].append(s[i])
        for key in hash:
            hash[key].sort(reverse=True)
        res = ''
        
        for i in range(len(s)):
            res += hash[find(i)].pop()
        return res
        
        