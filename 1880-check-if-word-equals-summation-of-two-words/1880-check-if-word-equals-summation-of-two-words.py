class Solution:
    def isSumEqual(self, f: str, s: str, t: str) -> bool:
        
        words = []
        
        for word in [f,s,t]:
            words.append(int(''.join([str(ord(c) - ord("a")) for c in word])))
        return sum(map(int,words[:2])) == int(words[-1])