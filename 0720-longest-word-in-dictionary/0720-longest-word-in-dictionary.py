class Solution:
    def longestWord(self, words: List[str]) -> str:
        built = set()
        built.add('')
        ans=''
        for w in sorted(words):
            if w[:-1] in built:
                built.add(w)
                if len(ans) < len(w) or len(ans) == len(w) and w < ans:
                    ans = w
        return ans