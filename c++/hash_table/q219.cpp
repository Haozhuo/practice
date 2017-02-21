bool containsNearbyDuplicate(vector<int>& nums, int k) {
    unordered_map<int,int> um;
    for(int i = 0; i < nums.size(); i++){
        unordered_map<int,int>::iterator it = um.find(nums[i]);
        if(it == um.end())
            um[nums[i]] = i;
        else{
            if(i-it->second<=k)
                return true;
            it->second = i;
        }
    }
    
    return false;
}
