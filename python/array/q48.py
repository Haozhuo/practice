def rotate(self, matrix):
    """
    :type matrix: List[List[int]]
    :rtype: void Do not return anything, modify matrix in-place instead.
    """
    for i in range(0,len(matrix)):
        for j in range(i+1,len(matrix)):
            matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]

    for i in range(0,len(matrix)):
        matrix[i].reverse()

        
void anti_rotate(vector<vector<int>>& matrix) {
    //take transpose and reverse reverse up-side-down
    for(int i = 0; i < matrix.size(); i++){
        for(int j = 0; j < matrix.size(); j++)
            swap(matrix[i][j],matrix[j][i]);
    }

    reverse(matrix.begin(),matrix.end());
}
