class Solution:
    def substringXorQueries(self, s: str, queries: List[List[int]]) -> List[List[int]]:
        mp = defaultdict(list)
        
        n = len(s)
        
        for i in range(n):
            curr = 0
            for j in range(i,min(i+30,n)):
                curr = curr * 2 + int(s[j])
                if curr not in mp:
                    mp[curr] = [i,j]
                else:
                    if mp[curr][1] - mp[curr][0] > j-i:
                        mp[curr] = [i,j]
        res = []
        
        for f,s in queries:
            t = f^s
            if t in mp:
                res.append(mp[t])
            else:
                res.append([-1,-1])
        return res