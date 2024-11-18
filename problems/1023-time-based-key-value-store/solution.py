class Entry:
    def __init__(self, value, timestamp):
        self.val = value
        self.time = timestamp

class TimeMap:

    def __init__(self):
        self.store = collections.defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append(Entry(value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""
        values = self.store[key]

        l = 0
        r = len(values) - 1


        targetTime = timestamp
        maxPrev = Entry("", -float("infinity"))
        while l <= r:
            m = l + (r - l) // 2

            if targetTime > values[m].time:
                if maxPrev.time < values[m].time:
                    maxPrev = values[m]
                l = m + 1
            elif targetTime < values[m].time:
                r = m - 1
            else:
                return values[m].val
        
        return maxPrev.val

        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
