class TimeMap:

    def __init__(self):
        self.store = collections.defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append({"val": value, "time": timestamp})

    def get(self, key: str, timestamp: int) -> str:
        ans = {"val": "", "time": 0}

        if key in self.store and self.store[key]:
            entries = self.store[key]
            l, r = 0, len(entries) - 1
            
            while l <= r:
                m = l + (r - l) // 2

                if entries[m]["time"] > timestamp: # lower half
                    r = m - 1
                elif entries[m]["time"] < timestamp: # upper half
                    l = m + 1
                    # record m as prev option
                    if entries[m]["time"] >= ans["time"]:
                        ans = entries[m]
                else:
                    return entries[m]["val"]
        
        return ans["val"]
            






# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
