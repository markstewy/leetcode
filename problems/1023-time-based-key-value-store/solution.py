class TimeMap:

    def __init__(self):
        self.values = collections.defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.values[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        ans = ""
        
        if key not in self.values:
            return ans

        times = self.values[key]
        l = 0
        r = len(times) - 1
        target = timestamp

        while l <= r:
            m = l + (r - l) // 2

            if target > times[m][0]:
                l = m + 1
                ans = times[m][1]
            elif target < times[m][0]:
                r = m - 1
            else:
                return times[m][1]
        
        return ans

        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
