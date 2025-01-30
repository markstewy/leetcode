class Node:
    def __init__(self, clss: int):
        self.clss = clss
        self.prereqs = []

class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        self.ans = [False] * len(queries)
        map = collections.defaultdict(list)

        for p in prerequisites:
            clss = p[1]
            pr = p[0]
            map[clss].append(pr)

        def helper(clss, target, i, visited):
            if clss in visited:
                return
            visited.add(clss)

            if clss == target:
                self.ans[i] = True
            if clss in map:
                for c in map[clss]:
                    helper(c, target, i, visited)
            else:
                return
        
        for i, q in enumerate(queries):
            clss = q[1]
            pr = q[0]
            helper(clss, pr, i, set())
        
        return self.ans


            






        


    

