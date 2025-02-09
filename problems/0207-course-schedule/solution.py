class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = collections.defaultdict(list)
        for crs, pr in prerequisites:
            preMap[crs].append(pr)
        

        circular, completed = set(), set()
        def helper(crs):
            if crs in circular:
                return False
            if crs in completed:
                return True
            
            circular.add(crs)
            for pr in preMap[crs]:
                if helper(pr) == False:
                    return False
            circular.remove(crs)

            # if we reach this point is has no prereqs or all prereqs are complete-able
            completed.add(crs)
            return True
        
        for crs in range(numCourses):
            if helper(crs) == False:
                return False
        return True
