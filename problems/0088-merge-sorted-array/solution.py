class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        dq2 = deque(nums2)
        dq1 = deque(nums1[:m])
        i = 0

        while dq1 or dq2:
            val1 = dq1[0] if dq1 else float("infinity")
            val2 = dq2[0] if dq2 else float("infinity")

            if val1 <= val2:
                nums1[i] = dq1.popleft()
            else:
                nums1[i] = dq2.popleft()
            
            i += 1
        
        
            



