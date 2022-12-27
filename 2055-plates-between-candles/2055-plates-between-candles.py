class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        n = len(s)
        prefix = [1 if c == "*" else 0 for c in s ]
        left = [-1] * n
        right = [-1] * n

        for i in range(1, n):
            prefix[i] += prefix[i-1]
        prefix = [0] + prefix
        lastLeft = -1
        lastRight = -1
        for i in range(n):
            if s[i] == '|':
                lastLeft = i
            if s[~i] == "|" :
                lastRight = n - i - 1
            left[i] = lastLeft
            right[~i] = lastRight
        for i, (s, e) in enumerate(queries):
            
            r , l = right[s],left[e] 
            if l == -1 or r == -1 or  l - 1 <= r: queries[i] = 0
            else : queries[i] = prefix[l+1] - prefix[r]
        return queries