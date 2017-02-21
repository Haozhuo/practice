#include <vector>
int maxProfit(vector<int>& prices) {
    int min_p = INT_MAX;
    int diff = 0;
    for(int i = 0; i < prices.size(); i++){
        if(prices[i] < min_p)
            min_p = prices[i];
        else if(prices[i]-min_p>diff)
            diff = prices[i] - min_p;
    }

    return diff;
}
