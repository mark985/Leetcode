class Codec:

    alphabet = string.ascii_letters + "0123456789"

    def __init__(self):
        self.url2Code = {}
        self.code2Url = {}

    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.
        
        :type longUrl: str
        :rtype: str
        """
        while longUrl is not self.url2Code:
            code = ''.join(random.choice(Codec.alphabet) for _ in range(6))
            if code is not self.code2Url:
                self.url2Code[longUrl] = code
                self.code2Url[code] = longUrl
        return "http:://tinyUrl.com/" + self.url2Code[longUrl]

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.
        
        :type shortUrl: str
        :rtype: str
        """
        return self.code2Url[shortUrl[-6:]]
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))