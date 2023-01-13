class Solution:
    def groupStrings(self, words: List[str]) -> List[int]:
        parent = list(range(len(words)))
        count = [1] * len(words)
        oneoff = {}
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
        
        seen = defaultdict(int)
        for i, word in enumerate(words):
            code = 0
            for w in word:
                asc = ord(w) - ord('a')
                code |= (1 << asc)
            if code in seen:
                count[seen[code]] += 1
            else :
                seen[code] = i
        for code in seen:
            for j in range(26):
                if (code >> j & 1) == 0 :
                    if code ^ 1 << j in seen:
                        union(seen[code], seen[code ^ 1 << j])
                else :
                    if  code ^ 1 << j in oneoff:
                        union(seen[code], seen[oneoff[code ^ (1 << j)]])
                    else :
                        oneoff[code ^ 1 << j] = code
        groups = defaultdict(int)
        for code in seen:
            groups[find(seen[code])] += 1
        return [len(groups), max(count)]
            
                        