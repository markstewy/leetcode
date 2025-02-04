class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        prmap = collections.defaultdict(list)
        for pr, crs in prerequisites:
            prmap[crs].append(pr)

        def helper(crs, target, circular: set[int]):
            if crs == target:
                return True
            if crs in circular:
                return False
            
            circular.add(crs)
            for c in prmap[crs]: # if any of the paths have the pr return True
                if helper(c, target, circular) == True:
                    return True
            
            return False
        
        ans = []
        for pr, crs in queries:
            ans.append(helper(crs, pr, set()))
        
        return ans


            






        


    

