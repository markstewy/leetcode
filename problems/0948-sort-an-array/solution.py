class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        def merge(lArr, rArr):
            k = max(len(lArr), len(rArr))
            ans = []
            l, r = 0, 0

            while l < len(lArr) or r < len(rArr):
                lv = lArr[l] if l < len(lArr) else float("infinity")
                rv = rArr[r] if r < len(rArr) else float("infinity")

                if lv < rv:
                    ans.append(lv)
                    l += 1
                else:
                    ans.append(rv)
                    r += 1
            return ans

        
        def mergeSort(arr):
            if len(arr) == 1:
                return arr

            m = len(arr) // 2
            l = mergeSort(arr[:m])
            r = mergeSort(arr[m:])

            return merge(l, r)
        
        return mergeSort(nums)
