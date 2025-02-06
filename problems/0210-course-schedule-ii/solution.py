class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preMap = collections.defaultdict(list)

        for crs, pre in prerequisites:
            preMap[crs].append(pre)


        circular = set() 
        completed = set()
        completedOrder = []

        def canComplete(crs):
            if crs in completed:
                return True
            if crs in circular:
                return False

            circular.add(crs)
            for pr in preMap[crs]:
                if canComplete(pr) == False:
                    return False
            circular.remove(crs)
                
            completed.add(crs)
            completedOrder.append(crs)
            return True
    
        for crs in range(numCourses):
            if canComplete(crs) == False:
                return []
        
        return completedOrder
