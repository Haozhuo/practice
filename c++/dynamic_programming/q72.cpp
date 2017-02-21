class Solution {
public:
    int minDistance(string word1, string word2) {
        int size1 = word1.size(); int size2 = word2.size();

        int **arr = new int*[size1+1];
        for(int i = 0; i < size1 + 1; i++){
            arr[i] = new int[size2+1];
            for(int j = 0; j < size2 + 1; j++){
                arr[i][j] = 0;
            }
        }

        for(int i = 1; i < size2 + 1; i++){
            arr[0][i] = i;
        }

        for(int j = 1; j < size1 + 1; j++)
            arr[j][0] = j;

        for(int i = 1; i  < size1 + 1; i++){
            for(int j = 1; j < size2 + 1; j++){
                int cost = word1[i-1] == word2[j-1] ? 0 : 1;
                arr[i][j] = min(min(cost+arr[i-1][j-1],1+arr[i-1][j]),1+arr[i][j-1]);
            }
        }

        return arr[size1][size2];

    }
};
