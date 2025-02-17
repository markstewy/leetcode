class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        self.prs = collections.defaultdict(list)
        for crs, pr in prerequisites:
            self.prs[crs].append(pr)
        
        self.order = []
        self.orderSet = set()
        self.visited = set()

        def isCompleteable(crs):
            if crs in self.visited:
                return False
            if crs in self.orderSet:
            # if crs not in self.prs or crs in self.orderSet:
                return True
            
            self.visited.add(crs)
            for pr in self.prs[crs]:
                if isCompleteable(pr) == False:
                    return False
            self.visited.remove(crs)

            self.orderSet.add(crs)
            self.order.append(crs)
            return True
            
        
        for crs in range(numCourses):
            if isCompleteable(crs) == False:
                return []
        return self.order
            
            
