class TimeMap:

    def __init__(self):
        self.values = collections.defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.values[key].append({"val": value, "time": timestamp})


    def get(self, key: str, timestamp: int) -> str:
        values = self.values[key]
        l, r = 0, len(values) - 1
        ans = ""

        while l <= r:
            m = l + (r - l) // 2
            if values[m]["time"] < timestamp:
                ans = values[m]["val"]
                l = m + 1
            elif values[m]["time"] > timestamp:
                r = m - 1
            else:
                return values[m]["val"]

        return ans      

 


        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
