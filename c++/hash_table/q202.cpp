//fast and slow pointer
class Solution {
public:
    bool isHappy(int n) {
        int fast = n;
        int slow = n;
        do{
            slow = square(slow);
            fast = square(fast);
            fast = square(fast);
        }while(fast != slow);
        if(slow == 1)
            return true;
        return false;

    }
private:
    int square(int num){
        int sum = 0;
        while(num != 0){
            sum += (num%10)*(num%10);
            num /= 10;
        }

        return sum;
    }
};
