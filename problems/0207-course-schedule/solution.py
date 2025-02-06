class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = collections.defaultdict(list)

        for crs, pr in prerequisites:
            preMap[crs].append(pr)

        visited = set()
        completed = set()
        def canComplete(crs: int) -> None:
            if crs in visited:
                return False
            if crs in completed:
                return True

            visited.add(crs)
            for pr in preMap[crs]:
                if canComplete(pr) == False:
                    return False
            visited.remove(crs)
        
            completed.add(crs)
            return True
        
        for crs in range(numCourses):
            if canComplete(crs) == False:
                return False
        return True


