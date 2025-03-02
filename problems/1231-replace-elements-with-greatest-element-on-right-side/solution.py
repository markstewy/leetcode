class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        rtlMax = []
        mx = 0
        for i in range(len(arr) - 1, -1, -1):
            if i == len(arr) - 1:
                rtlMax.append(-1)
                continue

            mx = max(mx, arr[i + 1])
            rtlMax.append(mx)
        rtlMax.reverse()

        return rtlMax

            
            
