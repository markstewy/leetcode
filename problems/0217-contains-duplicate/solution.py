class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nset = set()

        for n in nums:
            if n in nset:
                return True
            else:
                nset.add(n)
        
        return False
