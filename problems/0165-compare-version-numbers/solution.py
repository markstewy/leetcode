class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = [int(n) for n in version1.split(".")]
        v2 = [int(n) for n in version2.split(".")]

        for i in range(max(len(v1), len(v2))):
            val1 = v1[i] if i < len(v1) else 0
            val2 = v2[i] if i < len(v2) else 0

            if val1 < val2:
                return -1
            if val2 < val1:
                return 1
        return 0

