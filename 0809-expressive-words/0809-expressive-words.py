class Solution:
    def expressiveWords(self, s: str, words: List[str]) -> int:
        res = 0
        for word in words:
            i = 0
            j = 0
            while i < len(word) and j < len(s) and word[i] == s[j]:
                c = s[j]
                cnt1 = 0
                cnt2 = 0
                while i < len(word) and word[i] == c:
                    cnt1 += 1
                    i += 1
                while j < len(s) and s[j] == c:
                    j += 1
                    cnt2 += 1
                if cnt2 == 2 and cnt1 == 1 or cnt2 < cnt1:
                    break
            else:
                if j == len(s) and i == len(word):
                    res += 1
        return res