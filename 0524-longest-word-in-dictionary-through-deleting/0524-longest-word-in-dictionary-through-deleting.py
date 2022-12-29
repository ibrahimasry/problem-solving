class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        dictionary.sort()
        res = ""
        l = 0
        for word in dictionary:
            count = 0
            i = 0
            for c in s:
                if c == word[i]:
                    i += 1
                    count += 1
                    if i == min(len(s) , len(word)):
                        break 
            if count > l  and i == len(word):
                l = count
                res = word
        return res