class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        ans = 0

        for i in range(len(word)):
            if word[i] in "aeiou":
                j = i
                vset = set()
                while j < len(word) and word[j] in "aeiou":
                    vset.add(word[j])
                    j += 1
                    if len(vset) == 5:
                        ans += 1
        return ans

