class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = ""

        for i, c in enumerate(strs[0]):
            for word in strs:
                if i >= len(word) or word[i] != c:
                    return ans
            ans += c
        
        return ans
                

