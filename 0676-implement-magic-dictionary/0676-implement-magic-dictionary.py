class MagicDictionary:
    def __init__(self):
        self.hash = defaultdict(list)
    def buildDict(self, dictionary: List[str]) -> None:
        for word in dictionary:
            hash = self.hash
            for i , c in enumerate(word):
                hash[word[:i]+word[i+1:]].append([i,c])

    def search(self, w: str) -> bool:
        hash= self.hash
        for i, c in enumerate(w):
            curr = w[:i] + w[i+1:]
            if curr in hash:
                pairs = hash[curr]
                for j, k in pairs:
                    if j == i and c != k:
                        return True
        
        return False

# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dictionary)
# param_2 = obj.search(searchWord)