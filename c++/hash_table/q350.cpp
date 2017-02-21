vector<int> intersect(vector<int>& nums1, vector<int>& nums2) {
    //Method 1 Time:O(m+n) Space:O(m)
    unordered_map<int,int> um;
    vector<int> res;

    for(int i = 0; i < nums1.size(); i++)
        um[nums1[i]]++;
    for(int i = 0; i < nums2.size(); i++){
        if(um.find(nums2[i]) != um.end() && um[nums2[i]] > 0){
            um[nums2[i]]--;
            res.push_back(nums2[i]);
        }
    }

    return res;
}

vector<int> intersect(vector<int>& nums1, vector<int>& nums2) {
    //Method 2 Time:O(max(m,n)log(max(m,n))) Space:O(m)
    sort(nums1.begin(),nums1.end());
    sort(nums2.begin(),nums2.end());
    vector<int> res;
    int i1 = 0; int i2 = 0;

    while(i1 < nums1.size() && i2 < nums2.size()){
        if(nums1[i1]==nums2[i2]){
            res.push_back(nums1[i1]);
            i1++; i2++;
        }
        else if(nums1[i1] > nums2[i2])
            i2++;
        else
            i1++;
    }

    return res;
}
