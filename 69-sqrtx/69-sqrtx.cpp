class Solution {
public:
    int mySqrt(int x) {
        if (x == 0) return 0;
        if (x <= 3) return 1;
        
        double root = 2.0;
        
        while(true) {
            if (root * root == x) return root;
            if (root * root > x) return root - 0.5;
            root += 0.5;    
        }
    }
};