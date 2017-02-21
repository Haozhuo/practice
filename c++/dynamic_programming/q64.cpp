class Solution {
public:
    int minPathSum(vector<vector<int>>& grid) {
        int** arr = new int*[grid.size()];
        for(int i = 0; i < grid.size(); i++){
            arr[i] = new int[grid[0].size()];
        }

        arr[0][0] = grid[0][0];
        for(int i = 1; i < grid.size(); i++)
            arr[i][0] = (grid[i][0]+arr[i-1][0]);

        for(int j = 0; j < grid[0].size(); j++)
            arr[0][j] = (grid[0][j]+arr[0][j-1]);

        for(int i = 1; i < grid.size(); i++){
            for(int j = 1; j < grid[0].size(); j++){
                arr[i][j] = (min(arr[i-1][j],arr[i][j-1])) + grid[i][j];
            }
        }

        return arr[grid.size()-1][grid[0].size()-1];
    }
};
