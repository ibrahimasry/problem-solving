class Solution:
    def oddString(self, words: List[str]) -> str:
        
        counter = defaultdict(list)
        
        for word in words:
            diff = tuple(((ord(c2) -ord("a")) - (ord(c1) - ord('a')) + 26) % 26 for c1,c2 in zip(word,word[1:]))
            if diff in counter:
                counter[diff] = [word, counter[diff][1] + 1]
            else :
                counter[diff] = [word, 1]
        for key in counter:
            if counter[key][1] == 1:
                return counter[key][0]
            