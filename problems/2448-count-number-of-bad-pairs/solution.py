class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        diffs = [n - i for i, n in enumerate(nums)]
        count = Counter(diffs)
        # if two have the same diff, they will not be a bad pair
        print(diffs)

        badPairs = 0
        for i, n in enumerate(nums):
            possiblePairs = len(nums) - 1 - i
            badPairs += (possiblePairs - (count[n - i] - 1))
            count[n - i] -= 1
        
        return badPairs
            
