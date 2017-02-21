//derived from DP
//This is DP on the maximum profit I can get on a specific day(maybe sell it or not)
//max_val is obtained by max_val(if I do not sell today) and profits I sell today
class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int size = prices.size();
        if(size==0||size==1)
            return 0;

        int min_p = INT_MAX;
        int max_val = INT_MIN;

        for(int i = 0; i < size; i++){
            min_p = min(prices[i],min_p);
            max_val = max(max_val,prices[i]-min_p);
        }

        return max_val < 0 ? 0 : max_val;
    }
};


//traditional DP
//This is DP on if I sell on that specific day, what is the max value I can get
class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int size = prices.size();
        if(size==0||size==1)
            return 0;
        int max_val = 0;

        int *arr = new int[size];
        arr[0] = 0;
        for(int i = 1; i < size; i++){
            arr[i] = max(arr[i-1] + (prices[i] - prices[i-1]),0);
            max_val = max(max_val,arr[i]);
        }

        return max_val;
    }
};
