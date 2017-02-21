class Solution {
public:
    bool wordBreak(string s, vector<string>& wordDict) {
        unordered_set<string> us(wordDict.begin(),wordDict.end());
        int size = s.size();
        bool *arr = new bool[size+1];
        arr[0] = true;
        for(int i = 1; i < size + 1; i++)
            arr[i] = false;

        for(int i = 1; i < size + 1; i++){
            for(int j = 0; j < i; j++){
                //here, we use s.substr(j,i-j) since in arr, j represent whether there is a match on jth character(1-based)
                //but in array, we use 0-based index. The i also represent ith character which is in i-1 index
                if(arr[j] && (us.find(s.substr(j,i-j)) != us.end())){
                    arr[i] = true;
                    break;
                }
            }
        }

        for(int i = 0; i < size + 1; i++)
            cout << arr[i] << endl;

        return arr[size];
    }
};
