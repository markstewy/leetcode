class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preMap = collections.defaultdict(list)
        for crs, pr in prerequisites:
            preMap[crs].append(pr)
        

        completed, circular = set(), set()
        completedOrder = []
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

            completed.add(crs)
            completedOrder.append(crs)
            return True
    
        for crs in range(numCourses):
            if helper(crs) == False:
                return []
        
        return completedOrder
