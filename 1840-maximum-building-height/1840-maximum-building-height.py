class Solution:
    def maxBuilding(self, n: int, rest: List[List[int]]) -> int:
        if not rest :
            return n - 1
        rest.append([1,0])
        
        rest.sort()
        m = len(rest)
        for i in range(1, m):
            rest[i][1] = min(rest[i][1] , rest[i-1][1] + rest[i][0] - rest[i-1][0] )
        for i in range(m-2, -1, -1):
            rest[i][1] = min(rest[i][1] , rest[i+1][1] + rest[i+1][0] - rest[i][0])
        ans = 0
        
        for i in range(m-1):
            idx1, l1 = rest[i]
            idx2, l2 = rest[i+1]
            diff = abs(l2 - l1)
            dist = idx2 - idx1
            remain = dist - diff
            remain = remain//2
            ans = max(ans, max(l1, l2) + remain)
            
        return max(ans, rest[-1][1] + n - rest[-1][0])    