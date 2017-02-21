int maxProduct(vector<int>& nums) {
    if(nums.size()==0)
        return 0;
    int r = nums[0];
    int imax = r;
    int imin = r;
    for(int i = 1; i < nums.size(); i++){
        if(nums[i] < 0)
            swap(imax,imin);

        imax = max(nums[i],imax*nums[i]);
        imin = min(nums[i],imin*nums[i]);
        r = max(imax,r);
    }

    return r;
}

//traditional DP
//DP on what's the maximum value I can get if ended at this point
int maxProduct(vector<int>& nums) {
    int size = nums.size();
    if(size==0)
        return 0;
    int *pos = new int[size];
    int *neg = new int[size];
    int max_val = nums[0];
    pos[0] = neg[0] = nums[0];

    for(int i = 1; i < size; i++){
        pos[i] = max(max(pos[i-1]*nums[i],neg[i-1]*nums[i]),nums[i]);
        neg[i] = min(min(neg[i-1]*nums[i],pos[i-1]*nums[i]),nums[i]);
        max_val = max(max_val,pos[i]);
    }

    return max_val;
}
