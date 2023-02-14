class Solution:
    def countVowels(self, word: str) -> int:
        curr = res = 0
        for i , c in enumerate(word):
            if c in ['a', 'e', 'i', 'o','u']: curr += i+1
            res += curr
        return res 