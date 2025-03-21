class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prs = collections.defaultdict(list)
        for crs, pr in prerequisites:
            prs[crs].append(pr)
        
        visiting = set()
        completed = set()

        def helper(crs):
            if crs in completed:
                return True
            if crs in visiting:
                return False
            
            visiting.add(crs)
            for pr in prs[crs]:
                if helper(pr) == False:
                    return False
            visiting.remove(crs)

            completed.add(crs)
            return True
        
        for crs in range(numCourses):
            if helper(crs) == False:
                return False
        return True
