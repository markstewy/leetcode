// solution in 8 minutes
class Solution {
public:
    vector<int> replaceElements(vector<int>& arr) {
        int last = arr.size() - 1;
        int max = arr[last];
        arr[last] = -1;
        
        for (int i = last - 1; i >= 0; i--) {
            int temp = arr[i];
            arr[i] = max;
            max = temp > max ? temp : max;
        }
        return arr;
    }
};
