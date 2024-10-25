class Solution:
    def findHighAccessEmployees(self, access_times: List[List[str]]) -> List[str]:
        access_times.sort(key=lambda x: x[1])
        employees = collections.defaultdict(list)

        for access in access_times:
            name = access[0]
            time = access[1]
            employees[name].append(time)

        ans = []
        for name, times in employees.items():
            if self.isHighFrequency(times):
                ans.append(name)
        
        return ans
    
    def isHighFrequency(self, accessTimes):
        if len(accessTimes) < 3:
            return False
        l = 0
        r = 2
        while r < len(accessTimes):
            if int(accessTimes[r]) - int(accessTimes[l]) < 100:
                return True
            l += 1
            r += 1
            
        return False


