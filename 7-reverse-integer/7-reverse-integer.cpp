#include <bits/stdc++.h>
class Solution {
public:
    int reverse(int x) {
        // -2,147,483,648 to 2,147,483,647
        
        // store pos/neg
        bool pos = true;
        if (x < 0) {
            pos = false;
        }
        // convert to string
        string str = std::to_string(x);
        // reverse
        string rev;
        for (int i = str.length() - 1; i >= 0; i--) {
            rev += str[i];
        }
        if (!pos) {
            str = str.substr(0, str.length() - 1);
        }
        // convert to long long int
        long long int revInt = std::stoll(rev);
        if (!pos) {
            revInt *= -1;
        }
        // if outside 32 bit range return zero
        if (revInt > INT_MAX || revInt < INT_MIN) {
            return 0;
        } else {
            return revInt;
        }
    }
};