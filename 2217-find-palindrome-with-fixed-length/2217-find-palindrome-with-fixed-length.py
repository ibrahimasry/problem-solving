class Solution:
    def kthPalindrome(self, queries: List[int], intLength: int) -> List[int]:
        
        half = (intLength -1 ) // 2
        base = 10 ** half
        res = [q-1 + base for q in queries]
        for i, r in enumerate(res):
            ans = str(r)
            ans = ans + ans[-1 - intLength%2::-1]
            res[i] = int(ans) if len(ans) <= intLength else -1
        return res