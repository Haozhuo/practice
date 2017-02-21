//Bit
int missingNumber1(vector<int>& nums) {
    int ans = 0;
    for(int i = 0; i < nums.size(); i++){
        ans ^= i;
        ans ^= nums[i];
    }

    ans ^= nums.size();
    return ans;
}

//Math
int missingNumber2(vector<int>& nums) {
    int n = nums.size();
    int sum = 0;
    for(int i = 0; i < nums.size(); i++)
        sum += nums[i];
    return (1+n)*n/2 - sum;
}


//Interesting
int missingNumber3(vector<int>& nums) {
    int sum = 0;
    for(int i = 0; i < nums.size(); i++)
        sum += (nums[i]-i);
    return nums.size() - sum;
}
