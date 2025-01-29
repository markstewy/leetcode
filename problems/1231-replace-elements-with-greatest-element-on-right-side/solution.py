class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        rtl = [-1]

        mx = -1
        for i in range(len(arr) - 2, -1, -1):
            mx = max(arr[i + 1], mx)
            rtl.append(mx)
        rtl.reverse()
        
        return rtl
      
