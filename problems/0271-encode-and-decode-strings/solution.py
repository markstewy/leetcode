class Codec:

    def encode(self, strs):
        """Encodes a list of strings to a single string.
        
        :type strs: List[str]
        :rtype: str
        """

        encoded = ""
        for s in strs:
            encoded += str(len(s)) + "#" + s
        return encoded
        

    def decode(self, s):
        """Decodes a single string to a list of strings.
        
        :type s: str
        :rtype: List[str]
        """
        decoded = []
        i = 0
        while i < len(s):
            l = ""
            while s[i] != "#":
                l += s[i]
                i += 1
            i += 1
            length = int(l)
            l = i
            r = i + length

            decoded.append(s[l : r])
            i = r
        
        return decoded
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))
