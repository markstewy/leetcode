class SparseVector:
    def __init__(self, nums: List[int]):
        self.idxs = {}
        for i, n in enumerate(nums):
            if n != 0:
                self.idxs[i] = n 

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        total = 0
        for k in vec.idxs.keys():
            if k in self.idxs:
                total += self.idxs[k] * vec.idxs[k]
        return total



# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)
