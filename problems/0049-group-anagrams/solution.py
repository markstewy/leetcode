class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = collections.defaultdict(list)

        for s in strs:
            uKey = [0] * 26
            for c in s:
                uKey[ord(c) - ord("a")] += 1
            
            groups[tuple(uKey)].append(s)
        
        return list(groups.values())
