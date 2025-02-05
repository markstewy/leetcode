class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        prmap = collections.defaultdict(list)
        for crs, pr in prerequisites:
            prmap[crs].append(pr)

        
        completed, circular = set(), set()
        completedOrder = []

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
            completedOrder.append(crs)
            return True
        
        for i in range(numCourses):
            if dfs(i) == False:
                return []
            
        return completedOrder
