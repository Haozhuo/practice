void moveZeroes(vector<int>& nums) {
    int s = 0;
    int e = 0;
    while(e < nums.size()){
        if(nums[e]==0)
            e++;
        else{
            if(nums[s]==0){
                swap(nums[s],nums[e]);
            }
            e++;
            s++;
        }
    }
}
