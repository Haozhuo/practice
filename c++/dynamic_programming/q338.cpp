class Solution {
public:
    vector<int> countBits(int num) {
        vector<int> ans(num+1,0);

        for(int i = 0; i < num+1; i++){
            ans[i] = ans[i >> 1] + (i & 1);
        }
        return ans;
    }
};

class Solution {
public:
    vector<int> countBits(int num) {
        int *arr = new int[num + 1];
        int i = 0; int b = 1;

        while(b <= num){
            while(i < b && i + b <= num){
                arr[i+b] = arr[i] + 1;
                i++;
            }

            b <<= 1;
            i = 0;
        }

        vector<int> ans(arr,arr+num+1);
        return ans;

    }
};
