class Solution {
public:
    vector<int> replaceElements(vector<int>& arr) {
        int last = arr.size() - 1;
        int max = arr[last];
        arr[last] = -1;
        last--;
        
        for (int i = last; i >= 0; i--) {
            int temp = arr[i];
            arr[i] = max;
            max = max > temp ? max : temp;
        }
        return arr;
    }
};
