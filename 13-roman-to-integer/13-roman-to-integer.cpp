class Solution {
public:
    int romanToInt(string s) {
        std::unordered_map<std::string, int> numerals;
        numerals["I"] = 1;
        numerals["V"] = 5;
        numerals["X"] = 10;
        numerals["L"] = 50;
        numerals["C"] = 100;
        numerals["D"] = 500;
        numerals["M"] = 1000;
        
        numerals["IV"] = 4;
        numerals["IX"] = 9;
        numerals["XL"] = 40;
        numerals["XC"] = 90;
        numerals["CD"] = 400;
        numerals["CM"] = 900;
        
        int total = 0;
        for (int i = 0; i < s.length(); i++) {
            if (i == s.length() - 1 ) {
                total += numerals[s.substr(i, 1)];
                continue;
            }
            string sub = s.substr(i, 2);
            if (numerals.find(sub) != numerals.end()) {
                total += numerals[sub];
                i++;
            } else {
                total += numerals[s.substr(i, 1)];
            }
        }
        return total;
    }
};