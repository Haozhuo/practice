int lengthOfLongestSubstring(string s) {
    unordered_set<char> us;
    int b = 0; int e = 0; int max_len = 0;

    while(e < s.size() && b < s.size()){
        if(us.find(s[e]) == us.end()){
            us.insert(s[e]);
            e++;
        }
        else{
            max_len = max(max_len,e-b);
            us.erase(us.find(s[b]));
            b++;
        }
    }

    max_len = max(max_len,e-b);

    return max_len;
}
