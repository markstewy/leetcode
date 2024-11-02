class TimeMap:

    def __init__(self):
        self.store = collections.defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append({"time": timestamp, "val": value})

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store or not self.store[key]:
            return ""

        values = self.store[key]
        l = 0
        r = len(values) - 1
        maxprev = {"time": -1, "val": ""}
         
        while l <= r:
            m = l + (r - l) // 2

            if values[m]["time"] < timestamp:
                if values[m]["time"] > maxprev["time"]:
                    maxprev = values[m]
                l = m + 1
            elif values[m]["time"] > timestamp:
                r = m - 1
            else:
                return values[m]["val"]
        
        return maxprev["val"]
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
