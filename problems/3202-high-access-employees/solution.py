class Solution:
    def findHighAccessEmployees(self, times: List[List[str]]) -> List[str]:
        
        # sort by time
        # two pointers logic: remove l if outside the window, add r and check if 3 or more
        # use a set of names to avoid duplicats 

        times.sort(key=lambda x: int(x[1]))

        highAccess= set()
        empCount = {}
        l = 0
        for r in range(len(times)):

            while int(times[r][1]) - int(times[l][1]) >= 100:
                name = times[l][0]
                empCount[name] -= 1
                l += 1
            
            name = times[r][0]
            empCount[name] = empCount.get(name, 0) + 1
            if empCount[name] == 3:
                highAccess.add(name)
        
        return list(highAccess)
        
