class Solution:
    def findHighAccessEmployees(self, access_times: List[List[str]]) -> List[str]:
        access_times.sort(key=lambda x : int(x[1]))
        emps = {}
        ans = set()

        l = 0
        for r in range(len(access_times)):
            e, t = access_times[r]
            emps[e] = emps.get(e, 0) + 1

            while int(t) - 100 >= int(access_times[l][1]):
                e = access_times[l][0]
                emps[e] -= 1
                l += 1
            
            for e, c in emps.items():
                if c >= 3:
                    ans.add(e)
            
        return list(ans)

            
