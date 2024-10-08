class Solution:
    def myAtoi(self, s: str) -> int:
        if s == "":
            return 0

        s = s.lstrip(" ")
        sToInt = {
            "0": 0,
            "1": 1,
            "2": 2,
            "3": 3,
            "4": 4,
            "5": 5,
            "6": 6,
            "7": 7,
            "8": 8,
            "9": 9
        }

        maxInt = 2147483647
        minInt = -2147483648
        factor = 1
        total = 0
        start = -1
        negative = -1 if s and s[0] == "-" else 1

        for i, c in enumerate(s):
            if i == 0 and (s[i] == "-" or s[i] == "+"):
                continue
            if s[i].isdigit():
                start = i
            else:
                break
            

        for i in range(start, -1, -1):
            if s[i] == "-" or s[i] == "+":
                continue
            else:
                total += (factor * sToInt[s[i]]) * negative
                factor *= 10
                if total > maxInt:
                    return maxInt
                if total < minInt:
                    return minInt
        return total
        

