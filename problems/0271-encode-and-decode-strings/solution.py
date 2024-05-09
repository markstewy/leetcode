class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        encoded = ""

        for s in strs:
            encoded += str(len(s)) + "#" + s
        
        return encoded

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        i = 0
        ans = []

        while i < len(s):
            l = ""
            while s[i] != '#':
                l += s[i]
                i += 1
            i += 1
            end = i + int(l)
            ans.append(s[i : end])
            i = end
        return ans



# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))
