class Solution:
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        emps = collections.defaultdict(deque)
        keyTime = [ int(time.replace(":", "")) for time in keyTime ]
        times = list(zip(keyTime, keyName))
        times.sort()
        ans = set()

        for e in times:
            time, name = e[0], e[1]
            
            emps[name].append(time)

            while emps[name] and emps[name][0] < time - 100:
                emps[name].popleft()
            
            if len(emps[name]) >= 3:
                ans.add(name)
        
        ans = list(ans)
        ans.sort()
        return ans
