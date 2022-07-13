#include <string>
#include <math.h>

class Solution {
public:
    int titleToNumber(std::string columnTitle) {
        int columnCountTotal = 0;
        int baseLetterPosition = 0;
        
        for (int i = (int)columnTitle.length() - 1; i >= 0; i--) {
            bool isLastLetter = i == columnTitle.length() - 1;
            int letterValue = columnTitle[i] - 64;
            
            if (isLastLetter) {
                columnCountTotal += letterValue;
            } else {
                columnCountTotal += (letterValue * pow(26, baseLetterPosition));
            }
            baseLetterPosition++;
        }
        
        return columnCountTotal;
    }
};