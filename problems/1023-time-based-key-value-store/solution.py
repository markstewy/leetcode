class TimeMap:

    def __init__(self):
        self.map = collections.defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.map[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.map:
            return ""
        
        tArr = self.map[key]
        l = 0
        r = len(tArr) - 1

        closestPrev = ""
        while l <= r:
            m = l + (r - l) // 2
            if tArr[m][0] < timestamp:
                closestPrev = tArr[m][1]
                l = m + 1
            elif tArr[m][0] > timestamp:
                r = m - 1
            else:
                return tArr[m][1]
        
        return closestPrev

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
