class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        mc = max(candies)
        for i, n in enumerate(candies):
            diff = mc - n
            if diff <= extraCandies:
                candies[i] = True
            else:
                candies[i] = False
        return candies

        # Time O(n)
        # Space O(1)
