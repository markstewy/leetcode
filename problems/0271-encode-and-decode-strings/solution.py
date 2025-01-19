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
        ans = []
        i = 0
        while i < len(s):
            l = ""
            while s[i] != '#':
                l += s[i]
                print(l)
                i += 1
            i += 1

            word = s[i : i + int(l)]
            ans.append(word)
            i = i + int(l)

        return ans



# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))
