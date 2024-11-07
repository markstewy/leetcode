class Solution:
    def findHighAccessEmployees(self, access_times: List[List[str]]) -> List[str]:
        # sort by time and use a sliding window
        # track employee access in a map
        # if any have 3 or more access add them to the ans array

        ans = set()
        for i in range(len(access_times)):
            access_times[i][1] = int(access_times[i][1])
        
        access_times.sort(key=lambda x : x[1])

        emp = {}
        l = 0
        for r in range(len(access_times)):
            name = access_times[r][0]
            emp[name] = emp.get(name, 0) + 1

            while access_times[r][1] - access_times[l][1] >= 100:
                name = access_times[l][0]
                emp[name] -= 1
                l += 1
            
            for e, c in emp.items():
                if c >= 3:
                    ans.add(e)
        
        return list(ans)
