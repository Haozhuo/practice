class Solution {
public:
    int rob(vector<int>& nums) {
        int size = nums.size();
        if(size==0)
            return 0;
        if(size == 1)
            return nums[0];
        int *arr = new int[size+1];
        arr[0] = 0; arr[1] = nums[0];

        for(int i = 0; i < nums.size(); i++){
            if(i >= 1){
                arr[i+1] = max(nums[i]+arr[i+1-2],arr[i+1-1]);
            }
        }

        return arr[size];

    }
};
