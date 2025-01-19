class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = collections.defaultdict(list)

        for s in strs:
            ukey = [0] * 26
            for c in s:
                ukey[ord(c) - ord("a")] += 1 # [0, 2, 5, 0, 3,...]
            ans[tuple(ukey)].append(s)

        return list(ans.values())
            
            
