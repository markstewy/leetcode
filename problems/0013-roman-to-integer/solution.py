class Solution:
    def romanToInt(self, s: str) -> int:
        nums = {
            "I": 1,
            "II": 2,
            "III": 3,
            "IV": 4,
            "V": 5,
            "VI": 6,
            "VII": 7,
            "VIII": 8,
            "IX": 9,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
            "XL": 40,
            "XC": 90,
            "CD": 400,
            "CM": 900
        }

        subtotal = 0
        total = 0
        i = 0
        while i < len(s):

            four = s[i : i + 4] if i + 4 <= len(s) else ""
            three = s[i : i + 3] if i + 3 <= len(s) else ""
            two = s[i : i + 2] if i + 2 <= len(s) else ""
            one = s[i : i + 1] if i + 1 <= len(s) else ""

            if four in nums:
                total += nums[four]
                i += 4
            elif three in nums:
                total += nums[three]
                i += 3
            elif two in nums:
                total += nums[two]
                i += 2
            elif one in nums:
                total += nums[one]
                i += 1
        
        return total

            

