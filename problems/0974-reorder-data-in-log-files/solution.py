class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        dlogs = []
        llogs = []

        for l in logs:
            if l[-1].isdigit():
                dlogs.append(l)
            else:
                llogs.append(l)
        
        llogs.sort(key=lambda x : (x.split(" ")[1:], x.split(" ")[:1]))

        return llogs + dlogs
