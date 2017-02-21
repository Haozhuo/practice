class Solution {
public:
    vector<string> summaryRanges(vector<int>& nums) {
        vector<string> ret;
        int s = 0; int e = 0;
        for(int i = 1; i <= nums.size(); i++){
            if(i == nums.size() || nums[i] - nums[i - 1] != 1){
                e = i - 1;
                ret.push_back(print(s,e,nums));
                s = i;
            }
        }

        return ret;
    }
private:
    string print(int s, int e,vector<int>& nums){
        if(s==e)
            return to_string(nums[s]);
        else
            return to_string(nums[s]) + "->" + to_string(nums[e]);
    }
};
