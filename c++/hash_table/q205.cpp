bool isIsomorphic(string s, string t) {
    unordered_map<char,char> umf;
    unordered_map<char,char> umb;

    for(int i = 0; i < s.size(); i++){
        unordered_map<char,char>::iterator it = umf.find(s[i]);
        if(it == umf.end()){
            umf[s[i]] = t[i];
            umb[t[i]] = s[i];
        }
        else{
            if(it->second != t[i])
                return false;
        }
    }

    return umf.size() == umb.size();    
}
