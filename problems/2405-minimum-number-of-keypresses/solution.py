class Solution:
    def minimumKeypresses(self, s: str) -> int:
        count = {}

        for c in s:
            count[c] = count.get(c, 0) + 1
        
        sortedKeys = []

        for ch, cnt in count.items():
            sortedKeys.append((cnt, ch))
        sortedKeys.sort(reverse=True)
    
        pushCount = 0
        for i in range(len(sortedKeys)):
            factor = 1
            if i > 8:
                factor = 2
            if i > 17:
                factor = 3
            
            pushCount += sortedKeys[i][0] * factor
        
        return pushCount
        



                
