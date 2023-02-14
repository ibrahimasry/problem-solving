class Solution:
    def countVowels(self, word: str) -> int:
        seen = set(['a', 'e', 'i', 'o','u'])
        curr = 0
        res = 0
        
        for i , c in enumerate(word):
            if c in seen:
                curr += i+1
            res += curr
        return res 