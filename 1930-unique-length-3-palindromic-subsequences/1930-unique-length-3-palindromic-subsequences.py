class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        last = [-1] * 26
        first= [-1] * 26
        for i , c in enumerate(s):
            if first[ord(c)-ord('a')] == -1:
                first[ord(c) -ord('a')] = i
            else:
                last[ord(c) -ord('a')] = i
        ans = 0
        for i in range(26):
            if first[i] < last[i] and first[i] != -1:
                ans += len(set(s[first[i]+1:last[i]]))
        return ans
                    