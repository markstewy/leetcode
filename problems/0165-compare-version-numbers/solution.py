class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = deque([int(n) for n in version1.split(".")])
        v2 = deque([int(n) for n in version2.split(".")])

        while v1 or v2:
            v1Val = v1.popleft() if v1 else 0
            v2Val = v2.popleft() if v2 else 0

            if v1Val < v2Val:
                return -1
            if v1Val > v2Val:
                return 1
                
        return 0
