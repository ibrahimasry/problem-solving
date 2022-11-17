class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        
        lettersCount = Counter(letters)
        n = len(words)
        ans = 0
        
        
        def dp(start, lettersCount, scores):
            nonlocal ans
            ans = max(ans, scores)
            
            for i in range(start, n):
                copiedLetters = copy.deepcopy(lettersCount)
                word = words[i]
                currScore = 0
                isValid = True
                for c in word:
                    if c in copiedLetters and copiedLetters[c] > 0 :
                        copiedLetters[c] -= 1
                        currScore += score[ord(c) - ord("a")]
                    else:
                        isValid= False
                        break
                if isValid:
                    dp(i+1, copiedLetters, scores+currScore)
        dp(0, lettersCount, 0)
        return ans