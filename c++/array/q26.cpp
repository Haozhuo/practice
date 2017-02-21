int removeDuplicates(vector<int>& nums) {
    int s = 0;
    int e = 0;
    while(e < nums.size()){
        if(nums[s] != nums[e]){
            s++;
            nums[s] = nums[e];
        }
        e++;
    }

    return nums.size() == 0 ? s : s + 1;
}
