class Solution:
    def findHighAccessEmployees(self, atimes: List[List[str]]) -> List[str]:
        atimes.sort(key=lambda x : int(x[1]))
        emps = collections.defaultdict(deque)
        ans = set()
        
        for a in atimes:
            name = a[0]
            time = a[1]
            emps[name].append(int(time))

            while emps[name][0] <= int(time) - 100:
                emps[name].popleft()
            if len(emps[name]) >= 3:
                ans.add(name)
        
        return list(ans)

