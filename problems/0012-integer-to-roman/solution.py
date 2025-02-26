class Solution:
    def intToRoman(self, num: int) -> str:
        ans = []
        divisors = [[1000, "M"], [900, "CM"], [500, "D"], [400, "CD"], [100, "C"], [90, "XC"], [50, "L"], 
        [40, "XL"], [10, "X"], [9, "IX"], [5, "V"], [4, "IV"], [1, "I"]]

        for n, c in divisors:
            while num >= n:
                num -= n
                ans.append(c)
        
        return "".join(ans)

        
