class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        
        
        hash = defaultdict(lambda: inf)
        
        for u, v in paths:
            un = 0
            vn = 1
            hash[u] = min(un, hash[u])
            hash[v] = min(vn, hash[v])
        return max(hash.keys(), key=lambda x: hash[x])