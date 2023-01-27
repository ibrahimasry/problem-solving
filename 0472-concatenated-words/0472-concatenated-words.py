class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        def dp(word):
            if len(word) == 0:
                return True
            
            for i in range(len(word)+1):
                if word[:i] in seen and dp(word[i:]):
                    return True
            return False
        ans = []
        seen = set(words)
        for word in words:
            seen.remove(word)

            if(dp(word)):
                ans.append(word)
            seen.add(word)
        return ans