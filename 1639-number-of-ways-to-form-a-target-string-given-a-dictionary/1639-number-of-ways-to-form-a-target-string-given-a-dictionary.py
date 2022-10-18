class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        
        lru_cache(None)
        def dp(targetIndex, wordIndex):
            if targetIndex == len(target):
                return 1
            if wordIndex == len(words[0]):
                return 0
            if (targetIndex , wordIndex) in memo:
                return memo[(targetIndex, wordIndex)]
            ways = dp(targetIndex, wordIndex + 1)
            targetChar = target[targetIndex]
            if targetChar in count[wordIndex]:
                ways += dp(targetIndex + 1 , wordIndex + 1) * count[wordIndex][targetChar] 
            memo[(targetIndex, wordIndex)] = ways % mod
            return ways % mod
        
        count = [defaultdict(int) for _ in words[0]]
        mod = 10 ** 9 + 7
        wordLength = len(words[0])
        wordsLength = len(words)
        memo = defaultdict(tuple)
        for i in range(wordsLength):
            for j in range(wordLength):
                c = words[i][j]
                count[j][c] += 1
        return dp(0,0)