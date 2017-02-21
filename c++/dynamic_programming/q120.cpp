class Solution {
public:
    int minimumTotal(vector<vector<int>>& triangle) {
        int *arr = new int[triangle.size()];
        for(int i = 0; i < triangle.size(); i++)
            arr[i] = triangle[triangle.size()-1][i];

        for(int i = triangle.size() -2; i>=0; i--){
            for(int j = 0; j < triangle.size()-1; j++)
                arr[j] = triangle[i][j] + min(arr[j],arr[j+1]);
        }

        return arr[0];
    }
};
