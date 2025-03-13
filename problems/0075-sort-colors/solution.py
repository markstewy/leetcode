class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def merge(l, r, m):
            arr1 = deque(nums[l:m+1])  # Include m in the first half
            arr2 = deque(nums[m+1:r+1])  # Include r in the second half
            
            while arr1 or arr2:
                val1 = arr1[0] if arr1 else float("infinity")
                val2 = arr2[0] if arr2 else float("infinity")

                if val1 < val2:
                    nums[l] = arr1.popleft()
                else:
                    nums[l] = arr2.popleft()
                l += 1

        def mergeSort(l, r):
            if l == r:
                return
            
            m = l + (r - l) // 2
            mergeSort(l, m)
            mergeSort(m + 1, r)  # Start second half at m+1
            merge(l, r, m)  # Pass the correct boundaries

        mergeSort(0, len(nums) - 1)  # Don't forget to call the function


            
            




