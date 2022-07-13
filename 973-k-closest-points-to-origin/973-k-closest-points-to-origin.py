class Solution:
    
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def get_key(point: List[int]):
            return sqrt(pow(point[0], 2) + pow(point[1], 2))
        return sorted(points, key=get_key)[0:k]
        
        
