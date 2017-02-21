class Solution {
public:
    vector<vector<string>> groupStrings(vector<string>& strings) {
        unordered_map<string,vector<string>> um;
        vector<vector<string>> res;
        for(int i = 0; i < strings.size(); i++){
            um[shift(strings[i])].push_back(strings[i]);
        }
        for(unordered_map<string,vector<string>>::iterator it = um.begin(); it != um.end(); it++){
            vector<string> unit = it->second;
            sort(unit.begin(),unit.end());
            res.push_back(unit);
        }

        return res;
    }
private:
    string shift(string& s){
        string t = "";
        for(int i = 1; i < s.size(); i++){
            int diff = s[i] - s[i-1];
            if(diff < 0)
                diff += 26;
            t += ('a' + diff + ',');
        }
        return t;
    }
};
