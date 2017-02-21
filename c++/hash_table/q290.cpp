bool wordPattern(string pattern, string str) {
    unordered_map<char,string> umf;
    unordered_map<string,char> umb;
    vector<string> arr;
    string temp = "";

    for(int i = 0; i < str.size(); i++){
        if(str[i]==' '){
            arr.push_back(temp);
            temp = "";
        }
        else
            temp += str[i];
    }

    arr.push_back(temp);

    if(pattern.size() != arr.size())
        return false;

    for(int i = 0; i < min(pattern.size(),arr.size()); i++){
        unordered_map<char,string>::iterator it = umf.find(pattern[i]);
        if(it==umf.end()){
            umf[pattern[i]] = arr[i];
            umb[arr[i]] = pattern[i];
        }
        else{
            if(it->second != arr[i])
                return false;
        }
    }

    return umf.size() == umb.size();
}
