class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prmap = collections.defaultdict(list)

        for crs, pr in prerequisites:
            prmap[crs].append(pr)
        

        completed, circular = set(), set()
        def dfs(crs):
            if crs in completed:
                return True
            if crs in circular:
                return False
            
            circular.add(crs)
            for pr in prmap[crs]:
                if dfs(pr) == False:
                    return False
            circular.remove(crs)
            
            completed.add(crs)
            return True
        
        for i in range(numCourses):
            if dfs(i) == False:
                return False
            
        return True
