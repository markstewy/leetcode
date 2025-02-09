class Solution:
    def simplifyPath(self, path: str) -> str:
        parts = path.split("/")
        ans = []

        for p in parts:
            if p == "." or p == "":
                continue
            if p == "..":
                if ans:
                    ans.pop()
            else:
                ans.append(p)
        
        return "/" + "/".join(ans)
