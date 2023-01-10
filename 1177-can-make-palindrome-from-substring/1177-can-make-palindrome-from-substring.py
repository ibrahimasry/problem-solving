class Solution:
    def canMakePaliQueries(self, s: str, queries: List[List[int]]) -> List[bool]:
        prefix = [0]
        ans = []
        for c in s:
            code = ord(c) - ord('a')
            prefix.append(prefix[-1] ^ (1 << code))
        for l,r,c in queries:
            count = 0
            curr = prefix[r+1] ^ prefix[l]
            for i in range(32):
                if (curr >> i) & 1:
                    count += 1
            if count // 2 >  c :
                ans.append(False)
            else:
                ans.append(True)
        return ans