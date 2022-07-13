class Solution {
public:
    string addBinary(string a, string b) {
        int aIndex = a.length() - 1;
        int bIndex = b.length() - 1;
        int carry = 0;
        string result = "";
        
        while(aIndex >= 0 || bIndex >= 0 || carry > 0) {
            int aVal = 0;
            int bVal = 0;
            if (aIndex >= 0) aVal = a[aIndex] - '0';
            if (bIndex >= 0) bVal = b[bIndex] - '0';
            int ab = aVal + bVal + carry;
            
            switch(ab) {
                case 0:
                    carry = 0;
                    result = "0" + result;
                    break;
                case 1:
                    carry = 0;
                    result = "1" + result;
                    break;
                case 2:
                    carry = 1;
                    result = "0" + result;
                    break;
                case 3:
                    carry = 1;
                    result = "1" + result;
                    break;
            }
            aIndex--;
            bIndex--;
        }
        return result;
    }
};