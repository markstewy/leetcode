class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        mxdiag = 0
        mxarea = 0

        for dimension in dimensions:
            d = math.sqrt(dimension[0] ** 2 + dimension[1] ** 2)
            if d > mxdiag or (d == mxdiag and marea < dimension[0] * dimension[1]):
                mxdiag = d
                marea = dimension[0] * dimension[1]
        return marea
                
            
