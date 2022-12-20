class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        count = [[0] *  26 for _ in range(26)]
        ans = 0
        for a,b in words:
            a , b = ord(a) - ord('a') , ord(b) - ord('a')
            if count[b][a]:
                ans += 4
                count[b][a] -= 1
            else :
                count[a][b] += 1
        for i in range(26):
            if count[i][i]:
                ans += (count[i][i] * 2)
                break
        return ans