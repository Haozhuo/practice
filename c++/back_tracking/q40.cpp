vector<vector<int>> combinationSum2(vector<int>& candidates, int target) {
    vector<vector<int>> ret;
    vector<int> unit;
    if(candidates.size()==0)
        return ret;
    sort(candidates.begin(),candidates.end());
    recur(ret,unit,candidates,target,0,0,candidates.size());
    return ret;
}

    void recur(vector<vector<int>>& ans, vector<int>& unit, vector<int>& arr, int target,int sum,int s, int e){
    if(sum>target)
        return;
    if(sum==target){
        ans.push_back(unit);
        return;
    }
    else{
        int i = s;
        while(i < e){
            unit.push_back(arr[i]);
            recur(ans,unit,arr,target,sum+arr[i],i+1,e);
            i += 1;
            unit.pop_back();
            while(i < e && arr[i]==arr[i-1])
                i+=1;
        }
    }

}
