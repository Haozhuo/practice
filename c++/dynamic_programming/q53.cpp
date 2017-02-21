class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int size = nums.size();
        if(size==0)
            return 0;
        int sub = nums[0];
        int max_val = sub;

        for(int i = 1; i < size; i++){
            if(nums[i]+sub <= nums[i])
                sub = nums[i];
            else
                sub += nums[i];
            max_val = max(max_val,sub);
        }

        return max_val;
    }
};
