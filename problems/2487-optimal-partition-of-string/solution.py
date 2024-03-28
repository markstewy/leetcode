class Solution:
    def partitionString(self, s: str) -> int:
        cache = set()
        ans = []

        start, end = 0, 0
        while end < len(s):
            # if end is in cache add sub and set start to end
            if s[end] in cache:
                ans.append(s[start: end])
                start = end
                cache.clear()
            # else expand the subtring to the right
            cache.add(s[end])
            end += 1

        return len(ans) + 1

        


