class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramDict = collections.defaultdict(list)

        for s in strs:
            ukey = [0] * 26
            for c in s:
                ukey[ord(c) - ord('a')] += 1
            anagramDict[tuple(ukey)].append(s)
        
        return anagramDict.values()
