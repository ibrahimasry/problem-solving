class Solution:
    def arrangeWords(self, text: str) -> str:
        hash = defaultdict(list)
        res = ''
        for word in text.split():
            hash[len(word)].append(word)
        for l in sorted(hash):
            sent = ' '.join(hash[l])
            if len(res):
                res += " " +  sent
            else :
                res += sent
        res = res[0].upper() + res[1:].lower()
        return res