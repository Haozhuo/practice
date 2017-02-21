vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
    vector<vector<int>> ret;
    vector<int> unit;
    if(candidates.size()==0)
        return ret;
    recur(ret,unit,candidates,target,0,0,candidates.size());
    return ret;
}

void recur(vector<vector<int>>& ans, vector<int>& unit, vector<int>& arr, int target,int sum,int s, int e){
    if(sum > target)
        return;
    if(sum==target){
        ans.push_back(unit);
        return;
    }
    else{
        for(int i = s; i < e; i++){
            unit.push_back(arr[i]);
            recur(ans,unit,arr,target,sum+arr[i],i,e);
            unit.pop_back();
        }
    }
}
