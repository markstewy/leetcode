// solution in 12 minutes
class Solution {
public:
    bool canPlaceFlowers(vector<int>& flowerbed, int n) {
        int i = 0;
        
       for (int i = 0; i < flowerbed.size(); i++) {
            if (n <= 0) break;
            if (flowerbed[i] == 1) {
                i++; // skip extra since next one won't be available
                continue;
            }
           
            bool left = i == 0 || flowerbed[i - 1] == 0;
            bool right = i == flowerbed.size() - 1 || flowerbed[i + 1] == 0;
            if (right && left) {
                n--;
                flowerbed[i] = 1;
                i++; // skip one extra index since we know it won't be available
            }
        }
        return n <= 0;
    }
};
