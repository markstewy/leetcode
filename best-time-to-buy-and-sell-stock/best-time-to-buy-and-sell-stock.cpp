class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int maxProfit = 0;
        int minBuy = prices[0];
        for (int i = 1; i <= prices.size() - 1; i++) {
            minBuy = std::min(minBuy, prices[i]);
            maxProfit = std::max(prices[i] - minBuy, maxProfit);
        }
        return maxProfit;
    }
};