class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        def merge(lArr, rArr):
            ans = []
            ldq = deque(lArr)
            rdq = deque(rArr)
            
            while ldq or rdq:
                if not ldq:
                    ans.append(rdq.popleft())
                elif not rdq:
                    ans.append(ldq.popleft())
                elif ldq[0] <= rdq[0]:
                    ans.append(ldq.popleft())
                else:
                    ans.append(rdq.popleft())
            
            return ans   


        def mergeSort(arr):
            if len(arr) == 1:
                return arr
            
            m = len(arr) // 2
            l = mergeSort(arr[:m])
            r = mergeSort(arr[m:])

            return merge(l, r)
    
        return mergeSort(nums)
