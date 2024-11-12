class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        digitLogs = []
        alphaLogs = []

        for log in logs:
            if log[-1].isdigit():
                digitLogs.append(log)
            else:
                alphaLogs.append(log)

        alphaLogs.sort(key=lambda x : (x.split(" ")[1:], x.split(" ")[0:1]))

        return alphaLogs + digitLogs
