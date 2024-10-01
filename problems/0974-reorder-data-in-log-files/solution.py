class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        dLogs = [log for log in logs if log.split(" ")[1].isdigit()]
        aLogs = [log for log in logs if log.split(" ")[1].isalpha()]
        
        print(aLogs)
        print(dLogs)
        
        aLogs.sort(key = lambda x : (x.split(" ")[1:], x.split(" ")[0]))
        return aLogs + dLogs
