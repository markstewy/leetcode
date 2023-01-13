class Solution {
public:
    
    bool checkIsClear(vector<int>& flowerbed, int i) {
        if (flowerbed[i] == 1) return false;
        
        bool leftClear = (i - 1 < 0 || flowerbed[i - 1] == 0);
        bool rightClear = (i + 1 >= flowerbed.size() || flowerbed[i + 1] == 0);
        return leftClear && rightClear;
    }
    
    bool canPlaceFlowers(vector<int>& flowerbed, int n) {
        for (int i = 0; i < flowerbed.size(); i++) {
            if (checkIsClear(flowerbed, i)) {
                flowerbed[i] = 1;
                n--;
            }
        }
        return n <= 0;
    }
};
