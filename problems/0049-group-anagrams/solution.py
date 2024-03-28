class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # make a universal key
        ans = collections.defaultdict(list)

        for s in strs:
            s = s.lower()
            uKey = [0] *26

            for c in s:
                i = ord(c) - ord("a")
                uKey[i] += 1
            ans[tuple(uKey)].append(s)
        return ans.values()

