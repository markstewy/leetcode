class Solution:
    def intToRoman(self, num: int) -> str:
        ans = ""
        numerals = {
            1: "I",
            5: "V",
            10: "X",
            50: "L",
            100: "C",
            500: "D",
            1000: "M"
        }

        while num:
            divisors = list(numerals.keys())
            divisors.sort(reverse=True)
            for n in divisors:
                while num / n >= 1:
                    num -= n
                    ans += numerals[n]
        print(ans)
        ans = ans.replace("DCCCC", "CM").replace("CCCC", "CD")
        ans = ans.replace("LXXXX", "XC").replace("XXXX", "XL")
        ans = ans.replace("VIIII", "IX").replace("IIII", "IV")
    
        return ans


    

