class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        countArr = []

        for word in words:
            count = {}
            for c in word:
                count[c] = count.get(c, 0) + 1
            countArr.append(count)
        
        for c in countArr[0].keys():
            for count in countArr:
                if c not in count:
                    countArr[0][c] = 0
                else:
                    countArr[0][c] = min(countArr[0][c], count[c])
        
        ans = []
        for c, n in countArr[0].items():
            for i in range(n):
                ans.append(c)
        
        return ans
        
