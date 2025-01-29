class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        diffs = []
        ans = []

        for i in range(1, len(arr)):
            diffs.append([arr[i] - arr[i - 1], i])
        
        diffs.sort()
        mindiff = diffs[0][0]
        
        for diff in diffs:
            print(f"{diff} mindiff")
            if diff[0] == mindiff:
                r = diff[1]
                l = r - 1
                ans.append([arr[l], arr[r]])
            
        return ans

        






