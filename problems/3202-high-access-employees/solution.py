class Solution:
    def findHighAccessEmployees(self, access_times: List[List[str]]) -> List[str]:
        hae = set()
        count = {}
        times = [[int(time[1]), time[0]] for time in access_times]
        times.sort()

        l = 0
        for r in range(len(times)):
            while times[r][0] - times[l][0] >= 100:
                name = times[l][1] 
                count[name] -= 1 
                l += 1
            
            name = times[r][1]
            count[name] = count.get(name, 0) + 1
            if count[name] >= 3:
                hae.add(name)
        
        return list(hae)
