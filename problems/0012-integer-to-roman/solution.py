class Solution:
    def intToRoman(self, num: int) -> str:        
        ones = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
        tens = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
        hundreds = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
        thousands = ["", "M", "MM", "MMM"]

        ans = ""
        sNum = str(num)
        # 0123
        if len(sNum) >= 1:
            ans = ones[int(sNum[-1])]
        if len(sNum) >= 2:
            ans = tens[int(sNum[-2])] + ans
        if len(sNum) >= 3:
            ans = hundreds[int(sNum[-3])] + ans
        if len(sNum) == 4:
            ans = thousands[int(sNum[-4])] + ans
    
        return ans
        
            

        
        
        
        
