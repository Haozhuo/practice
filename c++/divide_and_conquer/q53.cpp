//NOTE: For DP methods, see python solutions

class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        if(nums.size()==0)
            return 0;
        int mx; int lmx; int rmx; int sum;
        maxSubArray(nums,0,nums.size()-1,mx,lmx,rmx,sum);

        return mx;
    }
private:
    void maxSubArray(vector<int>& nums, int l, int r, int& mx, int& lmx, int& rmx, int& sum){
        if(l>=r)
            mx = lmx = rmx = sum = nums[l];
        else{
            int mid = (l+r)/2;
            int mx1; int lmx1; int rmx1; int sum1;
            int mx2; int lmx2; int rmx2; int sum2;
            mx1 = mx2 = lmx1 = lmx2 = rmx1 = rmx2 = sum1 = sum2 = 0;
            maxSubArray(nums,l,mid,mx1,lmx1,rmx1,sum1);
            maxSubArray(nums,mid+1,r,mx2,lmx2,rmx2,sum2);
            mx = max(max(mx1,mx2),rmx1+lmx2);
            lmx = max(lmx1,sum1+lmx2);
            rmx = max(rmx2,sum2+rmx1);
            sum = sum1 + sum2;
        }
    }
};
