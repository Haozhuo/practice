class Solution {
public:
    int hammingWeight(uint32_t n) {
        //straigh-forward way
        int mask = 1;
        int sum = 0;
        for(int i= 0; i < 32; i++){
            if((n & mask) != 0){
                sum++;
            }
            mask <<= 1;
        }

        return sum;
    }
};

class Solution {
public:
    int hammingWeight(uint32_t n) {
        //smarter way
        int sum = 0;
        while(n != 0){
            n &= (n-1);
            sum++;
        }

        return sum;
    }
};
