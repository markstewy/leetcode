class TimeMap:

    def __init__(self):
        self.store = collections.defaultdict(list)
        
    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""
        
        values = self.store[key]
        target = timestamp
        nearestPrev = ""

        l = 0
        r = len(values) - 1
        
        while l <= r:
            m = l + (r - l) // 2

            if values[m][0] < target:
                nearestPrev = values[m][1]
                l = m + 1
            elif values[m][0] > target:
                r = m - 1
            else:
                return values[m][1]
        
        return nearestPrev
        
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
