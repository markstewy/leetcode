class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = collections.defaultdict(list)

        for s in strs:
            s = s.lower()
            # create a uinversal key from the string
            uKey = [0] * 26
            for c in s:
                uKey[ord(c) - ord("a")] += 1
            
            ans[tuple(uKey)].append(s)
        return ans.values()

