class Codec:
    alpha = string.ascii_letters + "123456790"
    def __init__(self):
        self.codeToLong = {}
    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        res = "http://tinyurl.com/"
        path = longUrl.split('/')[1:]
        code = str([random.choice(self.alpha) for i in range(6)])
        self.codeToLong[code] = longUrl
        return res + code

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        code = shortUrl.split('/')[-1]
        if code in self.codeToLong:
            return self.codeToLong[code]
        else :
            return ''
# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))