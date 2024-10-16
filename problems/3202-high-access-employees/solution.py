class Solution:
    def findHighAccessEmployees(self, access_times: List[List[str]]) -> List[str]:
        ans = []
        # orgainze by employee, acces times chronological in access array
        employeeTimes = collections.defaultdict(list) # "name": [time1, time2, ...]
        for e in access_times:
            name = e[0]
            time = e[1]
            employeeTimes[name].append(time)

        for e in employeeTimes:
            employeeTimes[e].sort()
            # sliding window approach, if r - l < 1 hr countMax if countMax > 3 ans.append(name)
            times = employeeTimes[e]
            l = 0
            for r in range(len(times)):
                while int(times[r]) - int(times[l]) >= 100:
                    l += 1
                if (r - l) + 1 >= 3:
                    ans.append(e)
                    break

        return ans


