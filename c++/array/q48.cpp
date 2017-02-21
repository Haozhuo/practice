void rotate2(vector<vector<int>>& matrix) {
    //Method 2: take the transpose and reverse left and right
    for(int i = 0; i < matrix.size(); i++){
        for(int j = i + 1; j < matrix.size(); j++)
            swap(matrix[i][j],matrix[j][i]);
    }

    for(int i = 0; i < matrix.size(); i++)
        reverse(matrix[i].begin(),matrix[i].end());
}

void rotate1(vector<vector<int>>& matrix) {
    //Method 1: reverse up-side-down, swap the symmetry
    reverse(matrix.begin(),matrix.end());

    for(int i = 0; i < matrix.size(); i++){
        for(int j = i + 1; j < matrix.size(); j++)
            swap(matrix[i][j],matrix[j][i]);
    }
}

void anti_rotate(vector<vector<int>>& matrix) {
    //take transpose and reverse reverse up-side-down
    for(int i = 0; i < matrix.size(); i++){
        for(int j = 0; j < matrix.size(); j++)
            swap(matrix[i][j],matrix[j][i]);
    }

    reverse(matrix.begin(),matrix.end());
}
