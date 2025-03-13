class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        k = len(nums1) - len(nums2)
        for n in nums2:
            nums1[k] = n
            k += 1

        def merge(l, r, m):
            dq1 = deque(nums1[l:m+1])
            dq2 = deque(nums1[m+1:r+1])

            while dq1 or dq2:
                val1 = dq1[0] if dq1 else float("infinity")
                val2 = dq2[0] if dq2 else float("infinity")
                
                if val1 < val2:
                    nums1[l] = dq1.popleft() 
                else:
                    nums1[l] = dq2.popleft()
                l += 1

        def mergeSort(l, r):
            if l == r:
                return
            
            m = l + (r - l) // 2
            mergeSort(l, m)
            mergeSort(m+1, r)

            merge(l, r, m)
    
        mergeSort(0, len(nums1) - 1)
