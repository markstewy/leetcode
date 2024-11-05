class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        digitLogs, letterLogs = [], []

        for l in logs:
            if l[-1].isdigit():
                digitLogs.append(l)
            else:
                letterLogs.append(l)
        
        letterLogs.sort(key=lambda x : (x.split(" ")[1:], x.split(" ")[0 : 1]))

        return letterLogs + digitLogs
