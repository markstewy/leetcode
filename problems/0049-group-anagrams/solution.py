class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        count = collections.defaultdict(list)

        for s in strs:
            ukey = [0] * 26
            for c in s:
                ukey[ord(c) - ord("a")] += 1
            count[tuple(ukey)].append(s)
        
        return list(count.values())
        

