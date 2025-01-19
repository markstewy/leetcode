class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        emailSet = set()

        for e in emails:
            parts = e.split("@")
            domain = parts[1]
            name = parts[0].split("+")[0]
            name = "".join(name.split("."))

            emailSet.add(name + "@" + domain)
            
        return len(emailSet)
