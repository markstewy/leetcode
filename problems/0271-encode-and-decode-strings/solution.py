class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        encoded = ""
        for s in strs:
            encoded += str(len(s)) + '#' + s

        return encoded
        

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """

        decoded = []
        l = 0
        r = 0

        while r < len(s):
            if s[r] == '#':
                length = int(s[l:r])

                l = r + 1
                r = l + length
                decoded.append(str(s[l:r]))

                l = r
            r += 1

        return decoded



# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))
