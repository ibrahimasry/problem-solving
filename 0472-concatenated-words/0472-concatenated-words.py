class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        def dp(word):
            for i in range(len(word)):
                if word[:i+1] in seen and dp(word[i+1:]):
                    return True
            return not word
        ans = []
        seen = set(words)
        for word in words:
            seen.remove(word)
            if dp(word):
                ans.append(word)
            seen.add(word)
        return ans