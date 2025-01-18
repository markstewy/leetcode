class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        lett = []
        dig = []

        for l in logs:
            if l.split(" ")[1].isdigit():
                dig.append(l)
            else:
                lett.append(l)


        lett.sort(key=lambda x : (" ".join(x.split(" ")[1:]), x.split(" ")[0]))
        
        return lett + dig
