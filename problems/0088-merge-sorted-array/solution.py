class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = m
        for n in nums2:
            nums1[i] = n
            i += 1
        nums1.sort()
        return nums1

            
