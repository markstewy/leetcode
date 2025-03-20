class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        def merge(l, r, m):
            dq1 = deque(nums[l:m+1])
            dq2 = deque(nums[m+1:r+1])

            while dq1 or dq2:
                dq1val = dq1[0] if dq1 else float("infinity")
                dq2val = dq2[0] if dq2 else float("infinity")
                
                if dq1val < dq2val:
                    nums[l] = dq1.popleft()
                else:
                    nums[l] = dq2.popleft()
                l += 1

        def mergeSort(l, r):
            if l == r:
                return

            m = l + (r - l) // 2
            mergeSort(l, m)
            mergeSort(m+1, r)
            merge(l, r, m)
        
        mergeSort(0, len(nums) - 1)
        return nums
