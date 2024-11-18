class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letterLogs = []
        digitLogs = []

        for l in logs:
            if l[-1].isalpha():
                letterLogs.append(l)
            else:
                digitLogs.append(l)
        
        letterLogs.sort(key=lambda x : (x.split(" ")[1:], x.split(" ")[0:1]))
        return letterLogs + digitLogs
