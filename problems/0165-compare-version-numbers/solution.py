class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = deque([int(n) for n in version1.split(".")])
        v2 = deque([int(n) for n in version2.split(".")])

        while v1 and v1[-1] == 0:
            v1.pop()
        while v2 and v2[-1] == 0:
            v2.pop()


        while v1 and v2:
            if v1[0] < v2[0]:
                return -1
            elif v1[0] > v2[0]:
                return 1
            else:
                v1.popleft()
                v2.popleft()
        
        if v1 and not v2:
            return 1
        if v2 and not v1:
            return -1
        if not v2 and not v1:
            return 0

