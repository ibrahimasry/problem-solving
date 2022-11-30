class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        
        n = len(s)
        start = 0
        ans = 0
        
        for c in range(2 * n):
            left = c // 2
            right = left + c % 2
            while start <= left and right < n and s[left] == s[right]:
                if right - left + 1 >= k :
                    ans +=1
                    start = right + 1
                    break
                left -= 1
                right += 1
        return ans
        