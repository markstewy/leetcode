class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = collections.defaultdict(list)

        for s in strs:
            ukey = [0] * 26
            for c in s:
                ukey[ord(c) - ord("a")] += 1
            anagrams[tuple(ukey)].append(s)
        
        return list(anagrams.values())
