class Solution:
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        keyTime = [int(n.replace(":", "")) for n in keyTime]
        times = list(zip(keyTime, keyName))
        times.sort()

        ans = set()

        empCount = {}

        l = 0
        for r, t in enumerate(times):
            time = t[0]
            name = t[1]
            empCount[name] = empCount.get(name, 0) + 1

            while times[l][0] < time - 100:
                empCount[times[l][1]] -= 1
                l += 1
            
            if empCount[name] >= 3:
                ans.add(name)
        
        names = list(ans)
        names.sort()
        return names
        









