int longestPalindrome(string s) {
    unordered_map<char,int> um;
    for(int i = 0; i < s.size(); i++)
        um[s[i]]++;

    int len = 0;
    bool flag = false;

    for(unordered_map<char,int>::iterator it = um.begin(); it != um.end(); it++){
        len += (it->second/2)*2;
        it->second = (it->second)%2;
        if(it->second == 1)
            flag = true;
    }

    return flag ? len + 1 : len;
}
