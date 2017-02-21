bool isAnagram(string s, string t) {
    if(s.size() != t.size())
        return false;

    unordered_map<char,int> um;
    for(int i = 0; i < s.size(); i++){
        um[s[i]]++;
    }

    for(int j = 0; j < t.size(); j++){
        unordered_map<char,int>::iterator it = um.find(t[j]);
        if(it == um.end())
            return false;
        else if(it->second <= 0)
            return false;
        else
            it->second--;
    }

    return true;
}
