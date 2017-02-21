#include <vector>
#include <iostream>
int majorityElement(vector<int>& nums) {
    int count = 0;
    int majority = 0;
    for(int i = 0; i < nums.size(); i++){
        if(!count){
            count = 1;
            majority = nums[i];
        }
        else{
            count += (nums[i]==majority) ? 1 : -1;
        }
    }

    return majority;
}
