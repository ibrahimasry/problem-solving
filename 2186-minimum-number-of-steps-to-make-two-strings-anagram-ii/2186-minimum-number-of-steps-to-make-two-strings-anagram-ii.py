class Solution:
    def minSteps(self, s: str, t: str) -> int:
        count1 = Counter(s)
        count2 = Counter(t)
        
        ans = 0
        
        for c in string.ascii_lowercase:
            ans += abs(count1[c] - count2[c])
        return ans