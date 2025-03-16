class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        dq1 = deque(nums1)
        dq2 = deque(nums2)
        for _ in range(len(nums2)):
            dq1.pop()

        i = 0
        while dq1 or dq2:
            dq1val = dq1[0] if dq1 else float("infinity")
            dq2val = dq2[0] if dq2 else float("infinity")
            if dq1val < dq2val:
                nums1[i] = dq1.popleft()
            else:
                nums1[i] = dq2.popleft()
            i += 1
            
