class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # keep track of most common character, use a map and get max(map.items())
        # two pointers l & r both start at index 0
        if len(s) == 0: return 0

        longest = 0
        count = {}

        l = 0
        for r, rChar in enumerate(s):
            # add r to the count:
            count[rChar] = count.get(rChar, 0) + 1

            # while is not valid move up left
            while (r - l + 1) - max(count.values()) > k:
                count[s[l]] = count[s[l]] - 1 # should never need to be initialized to zero
                l += 1
            
            # now that its valid, update longest
            longest = max(longest, (r - l + 1))
            
        return longest
