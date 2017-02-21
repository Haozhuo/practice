vector<string> findRepeatedDnaSequences(string s) {
    unordered_map<int, int> m;
    vector<string> r;
    if(s.size() <= 9)
        return r;
    int t = 0, i = 0, ss = s.size();
    while (i < 9){
         //treat each integer as 3 bits and merge 9 letters into a int
        t = t << 3 | s[i++] & 7;
    }
    while (i < ss){
        // t << 3 & 0x3fffffff is used to
        //(1) shift t by 3 and only use the lower 30 bits
        if (m[t = t << 3 & 0x3FFFFFFF | s[i++] & 7]++ == 1)
            r.push_back(s.substr(i - 10, 10));
    }

    return r;
}
