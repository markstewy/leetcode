class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # create a universal key from any anagram variation
        ans = collections.defaultdict(list)

        for s in strs:
            uKey = [0] * 26
            for c in s:
                uKey[ord(c) - ord("a")] += 1
            ans[tuple(uKey)].append(s)        
        return ans.values()
