class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1, v2 = version1.split("."), version2.split(".")
        
        length = max(len(v1), len(v2))
        
        for i in range(length):
            v1num = int(v1[i].lstrip("0")) if i < len(v1) and v1[i].lstrip("0") != '' else 0
            v2num = int(v2[i].lstrip("0")) if i < len(v2) and v2[i].lstrip("0") != '' else 0
            
            if v1num > v2num:
                return 1
            elif v1num < v2num:
                return -1
        return 0
