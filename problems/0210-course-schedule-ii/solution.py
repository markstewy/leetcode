class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        prs = defaultdict(list)
        for crs, pr in prerequisites:
            prs[crs].append(pr)
        

        completed = set()
        visiting = set()
        ans = []

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
            ans.append(crs)

            return True
        
        for crs in range(numCourses):
            if helper(crs) == False:
                return []
        
        return ans

