class TimeMap:

    def __init__(self):
        self.storage = {} # key: [(timestamp, value)]

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.storage:
            self.storage[key] = []
        self.storage[key].append((timestamp, value))
        
    def get(self, key: str, timestamp: int) -> str:
        values = self.storage.get(key, [])
        l = 0
        r = len(values) - 1
        ans = ""

        while l <= r:
            m = l + (r - l) // 2
            if values[m][0] <= timestamp:
                l = m + 1
                ans = values[m][1]
            else:
                r = m - 1
        return ans
            


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
