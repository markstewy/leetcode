class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        self.prs = collections.defaultdict(list)
        
        for crs, pr in prerequisites:
            self.prs[crs].append(pr)

        self.visited = set()
        self.isCompleteable = set()
        
        def canComplete(crs):
            if crs in self.visited:
                return False
            
            if crs not in self.prs or crs in self.isCompleteable:
                for crs in self.visited:
                    self.isCompleteable.add(crs)
                return True
            
            for pr in self.prs[crs]:
                self.visited.add(crs)
                if canComplete(pr) == False:
                    return False
                self.visited.remove(crs)
            return True
        
        for crs in range(numCourses):
            if canComplete(crs) == False:
                return False
        return True
