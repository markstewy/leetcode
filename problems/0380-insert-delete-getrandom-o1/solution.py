class RandomizedSet:

    def __init__(self):
        self.idxMap = {}
        self.nums = []
        
    def insert(self, val: int) -> bool:
        present = val in self.idxMap
        if not present:
            self.nums.append(val)
            self.idxMap[val] = len(self.nums) - 1
        return not present
        
    def remove(self, val: int) -> bool:
        present = val in self.idxMap
        if present:
            if len(self.nums) == 1 or self.nums[-1] == val:
                del self.idxMap[val]
                self.nums.pop()
            else:
                lastVal = self.nums[-1]
                targetIdx = self.idxMap[val]
                del self.idxMap[val]
                self.nums[targetIdx] = lastVal
                self.idxMap[lastVal] = targetIdx
                self.nums.pop()          
        return present
        
    def getRandom(self) -> int:
        return random.choice(self.nums)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
