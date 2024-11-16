class TimeMap:

    def __init__(self):
        self.store = collections.defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append({"time": timestamp, "val": value})

    def get(self, key: str, targetTime: int) -> str:
        mxprev = {"time": -1, "val": ""}

        if key not in self.store:
            return ""
        values = self.store[key]

        l = 0
        r = len(values) - 1
        while l <= r:
            m = l + (r - l) // 2
            mtime = values[m]["time"]

            if targetTime < mtime:
                r = m - 1
            elif mtime < targetTime:
                if mtime > mxprev["time"]:
                    mxprev = values[m]
                l = m + 1
            else:
                return values[m]["val"]
        
        return mxprev["val"]
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,targetTime)
# param_2 = obj.get(key,timestamp)
