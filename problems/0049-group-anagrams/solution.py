class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        ans = collections.defaultdict(list)

        for s in strs:
            ukey = [0] * 26
            for c in s:
                ukey[ord(c) - ord("a")] += 1
            ans[tuple(ukey)].append(s)
        
        return ans.values()
