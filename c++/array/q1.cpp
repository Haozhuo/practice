vector<int> twoSum(vector<int>& nums, int target) {
    unordered_map<int,int> rec;
    unordered_map<int,int>::iterator it;
    for(int i = 0; i < nums.size(); i++){
        rec.insert(make_pair(nums[i],i));
    }

    for(int i = 0; i < nums.size(); i++){
        int temp = target - nums[i];
        if(rec.find(temp) != rec.end() && rec.find(temp)->second != i){
            vector<int> ans;
            ans.push_back(i);
            ans.push_back(rec.find(temp)->second);
            return ans;
        }
    }

    vector<int> ans;
    return ans;
}
