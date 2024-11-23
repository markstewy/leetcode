class Solution:
    def findHighAccessEmployees(self, access_times: List[List[str]]) -> List[str]:
        access_times.sort(key=lambda x : int(x[1]))
        count = {}
        hfe = set()

        l = 0
        for r in range(len(access_times)):
            while int(access_times[l][1]) <= int(access_times[r][1]) - 100:
                emp = access_times[l][0]
                count[emp] -= 1
                l += 1
            
            emp = access_times[r][0]
            count[emp] = count.get(emp, 0) + 1

            if count[emp] >= 3:
                hfe.add(emp)
        
        return list(hfe)
