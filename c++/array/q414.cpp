//NOTE: Trakcing the largest 3 numbers
int thirdMax1(vector<int>& nums) {
    set<int> top3;
    for(int i = 0; i < nums.size(); i++){
        top3.insert(nums[i]);
        if(top3.size() > 3)
            top3.erase(top3.begin());
    }
    return top3.size() == 3 ? *top3.begin() : *top3.rbegin();
}


int thirdMax2(vector<int>& nums) {
    long f = LONG_MIN;
    long s = LONG_MIN;
    long t = LONG_MIN;

    for(int i = 0; i < nums.size(); i++){
        int temp = nums[i];
        if(f == temp || s == temp || t == temp)
            continue;
        if(temp > f){
            t = s;
            s = f;
            f = temp;
        }
        else if(temp > s){
            t = s;
            s = temp;
        }
        else if(temp > t){
            t = temp;
        }
    }

    return t == LONG_MIN ? f : t;
}
