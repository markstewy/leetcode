class Solution:
    def romanToInt(self, s: str) -> int:
        numerals = {
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

        total = 0
        i = 0
        while i < len(s):
            if  i < len(s) - 1 and s[i : i + 2] in numerals:
                numeral = s[i : i + 2]
                total += numerals[numeral]
                i += 2
            else:
                numeral = s[i : i + 1]
                total += numerals[numeral]
                i += 1
        
        return total

            
