class Solution:
    def findHighAccessEmployees(self, access_times: List[List[str]]) -> List[str]:
        # sliding window of 1 hour

        # remove timed out
        
        # add new (if 3 or more) add to the ans list
        for i in range(len(access_times)):
            access_times[i][1] = int(access_times[i][1])

        access_times.sort(key=lambda x : x[1])
        empCounter = collections.defaultdict(deque)
        ans = []

        l = 0
        for r in range(len(access_times)):
            # move up left if outside the new hour window
            while access_times[r][1] - access_times[l][1] >= 100:
                emp = access_times[l][0]
                empCounter[emp].popleft()
                l += 1
            
            # add the new emp access, if it is >= 3 add to high access list
            emp = access_times[r][0]
            time = access_times[r][1]
            empCounter[emp].append(time)
            
            if len(empCounter[emp]) >= 3 and emp not in ans:
                ans.append(emp)
        return ans


        


