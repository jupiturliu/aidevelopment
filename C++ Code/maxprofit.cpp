#include <iostream>
#include <vector>


// You are given an integer array prices where prices[i] is the price of a given stock on the ith day.
// On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the
// stock at any time. However, you can buy it then immediately sell it on the same day.
//Find and return the maximum profit you can achieve.

int maxProfit(const std::vector<int>& prices) {
    int max_profit = 0;
    for (size_t i = 1; i < prices.size(); ++i) {
        if (prices[i] > prices[i - 1]) {
            max_profit += prices[i] - prices[i - 1];
        }
    }
    return max_profit;
}

int main() {
    std::vector<int> prices = {7, 1, 5, 3, 6, 4};
    int profit = maxProfit(prices);
    std::cout << "Maximum profit: " << profit << std::endl;
    return 0;
}