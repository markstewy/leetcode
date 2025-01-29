class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxCandies = max(candies)
        result = [child + extraCandies >= maxCandies for child in candies]
        return result
