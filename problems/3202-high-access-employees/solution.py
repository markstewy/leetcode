class Solution:
    def findHighAccessEmployees(self, access_times: List[List[str]]) -> List[str]:

        access_times.sort(key=lambda x : int(x[1]))
        count = {}
        empSet = set()

        l = 0
        for r in range(len(access_times)):
            while int(access_times[r][1]) - int(access_times[l][1]) >= 100:
                name = access_times[l][0]
                count[name] -= 1
                l += 1
            
            name = access_times[r][0]
            count[name] = count.get(name, 0) + 1
            if count[name] >= 3:
                empSet.add(name)

        return list(empSet)
            
