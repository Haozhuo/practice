//divide and conquer
class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        return searchMatrix(matrix,target,0,matrix.size()-1);
    }
private:
    bool searchMatrix(vector<vector<int>>& matrix, int target, int s, int e){
        if(s > e)
            return false;
        if(s==e)
            return binary_search(matrix[s],target);

        int mid = s + (e-s)/2;
        bool result1 = searchMatrix(matrix,target,s,mid);
        if(result1)
            return true;
        else
            return searchMatrix(matrix,target,mid+1,e);
    }

    bool binary_search(vector<int>& vec,int target){
        if(vec.size() == 0)
            return false;
        int s = 0; int e = vec.size() - 1;

        while(s <= e){
            int mid = s + (e-s) / 2;
            if(vec[mid]==target)
                return true;
            else if(vec[mid] > target)
                e = mid - 1;
            else
                s = mid + 1;
        }

        return false;
    }
};
