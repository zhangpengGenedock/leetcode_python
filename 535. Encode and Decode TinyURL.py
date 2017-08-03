class Codec:

    # def __init__(self):
    #     self.urls = []
    #
    # def encode(self, longUrl):
    #     """Encodes a URL to a shortened URL.
    #
    #     :type longUrl: str
    #     :rtype: str
    #     """
    #     self.urls.append(longUrl)
    #     return 'http://tinyurl.com/' + str(len(self.urls) - 1)
    #
    # def decode(self, shortUrl):
    #     """Decodes a shortened URL to its original URL.
    #
    #     :type shortUrl: str
    #     :rtype: str
    #     """
    #     return self.urls[int(shortUrl.split('/')[-1])]

    import string
    alphabet = string.ascii_letters + '0123456789'

    def __init__(self):
        self.url2code = {}
        self.code2url = {}

    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.
        https://discuss.leetcode.com/topic/81637/two-solutions-and-thoughts/2
        :type longUrl: str
        :rtype: str
        """
        while longUrl not in self.url2code:
            import random
            code = ''.join(random.choice(Codec.alphabet) for _ in range(6))
            if code not in self.code2url:
                self.code2url[code] = longUrl
                self.url2code[longUrl] = code
        return 'http://tinyurl.com/' + self.url2code[longUrl]

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.
        https://discuss.leetcode.com/topic/81637/two-solutions-and-thoughts/2
        :type shortUrl: str
        :rtype: str
        """
        return self.code2url[shortUrl[-6:]]
