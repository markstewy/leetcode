class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        merged = {}
        for n, count in nums1:
            merged[n] = merged.get(n, 0) + count
        for n, count in nums2:
            merged[n] = merged.get(n, 0) + count
        
        ans = []
        for n, count in merged.items():
            ans.append([n, count])
        ans.sort()
        return ans
        
