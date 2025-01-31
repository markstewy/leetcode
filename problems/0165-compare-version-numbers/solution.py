class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = deque([int(n) for n in version1.split(".")])
        v2 = deque([int(n) for n in version2.split(".")])

        while v1 or v2:
            v1n = v1[0] if v1 else 0
            v2n = v2[0] if v2 else 0
            
            if v1n > v2n:
                return 1
            if v1n < v2n:
                return -1
            if v1:
                v1.popleft()
            if v2:
                v2.popleft()
        
        return 0


