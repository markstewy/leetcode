class Solution {
public:
    vector<int> replaceElements(vector<int>& arr) {
        int idx = arr.size() - 1;
        int max = arr[idx];
        arr[idx] = -1;
        idx--;
        
        for (; idx >= 0; idx--) {
            int tempMax = arr[idx];
            arr[idx] = max;
            
            max = max > tempMax ? max : tempMax;
        }
        return arr;
    }
};
