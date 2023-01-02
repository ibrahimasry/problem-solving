class StreamChecker(object):

    def __init__(self, words):
        """
        :type words: List[str]
        """
        Tri = lambda: defaultdict(Tri)
        self.tri = Tri()
        for w in words:
            reduce(defaultdict.__getitem__, w[::-1], self.tri)['#'] = True
        self.s = ""
        self.max = len(max(words,key=len))
    def query(self, letter):
        """
        :type letter: str
        :rtype: bool
        """
        tri = self.tri
        self.s = (letter + self.s)[:self.max]
        for c in self.s:
            if c in tri:
                tri = tri[c]
                if tri["#"] == True:
                    return True
            else:
                break
        
        return False
        


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)