class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        cache = set()

        for n in nums:
            if n in cache:
                return True
            cache.add(n)
        return False
