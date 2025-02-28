class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        prs = collections.defaultdict(list)
        for crs, pr in prerequisites:
            prs[crs].append(pr)

        visiting = set()
        completed = set()
        order = []

        def helper(crs):
            if crs in visiting:
                return False
            if crs in completed:
                return True

            # check all prs
            visiting.add(crs)
            for pr in prs[crs]:
                if helper(pr) == False:
                    return False
            visiting.remove(crs)

            completed.add(crs)
            order.append(crs)
            return True
        
        for crs in range(numCourses):
            if helper(crs) == False:
                return []
        return order
