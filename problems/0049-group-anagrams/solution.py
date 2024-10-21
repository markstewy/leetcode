class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        groups = collections.defaultdict(list)

        for s in strs:
            ukey = [0] * 26
            for c in s:
                ukey[ord(c) - ord("a")] += 1
            
            groups[tuple(ukey)].append(s)
        
        print(groups.values())
        return list(groups.values())
