class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {

        int zcount = 0;
        int tprod = 1;
        int tprod_exclude_zeros = 1;
         vector<int> sol;

        // Loop once to get zero count and product totals
        for (int n : nums) {
            if (n == 0) {
                zcount++;
            } else {
                tprod_exclude_zeros *= n;
            }
            tprod *= n;
        }

        // loop once more to create solution array
        if (zcount == 0) {
            for (int n : nums) {
                sol.push_back(tprod / n);
            }
        } else if (zcount == 1) {
            for (int n : nums) {
                if (n != 0) {
                    sol.push_back(0);
                } else {
                    sol.push_back(tprod_exclude_zeros);
                }
            }
        } else if (zcount > 1) {
            for (int n : nums) {
                sol.push_back(0);
            }
        }

        return sol;

    }
};
