class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        eset = set()
        count = 0

        for e in emails:
            parts = e.split("@")
            name = parts[0]
            domain = parts[-1]
            
            if "+" in name:
                name = name.split("+")[0]
            name = name.replace(".", "")

            if (name, domain) not in eset:
                count += 1
                eset.add((name, domain))

        return count
