class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        anagrams = collections.defaultdict(list)

        for s in strs:
            anagramKey = [0] * 26
            for c in s:
                anagramKey[ord(c) - ord("a")] += 1
            anagrams[tuple(anagramKey)].append(s)
        
        return anagrams.values()
