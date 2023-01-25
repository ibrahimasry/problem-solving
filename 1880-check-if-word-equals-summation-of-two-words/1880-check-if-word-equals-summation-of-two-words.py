class Solution:
    def isSumEqual(self, f: str, s: str, t: str) -> bool:
        
        words = []
        
        for word in [f,s,t]:
            words.append('')
            for c in word:
                words[-1] += str(ord(c) - ord("a"))
        return sum(map(int,words[:2])) == int(words[-1])