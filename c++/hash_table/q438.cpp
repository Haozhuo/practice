vector<int> findAnagrams(string s, string p) {
    int l = 0;
    int r = 0;
    int count = p.size();

    int* m  = new int[26];
    vector<int> ans;

    for(int i = 0; i < 26; i++)
        m[i] = 0;

    for(int i = 0; i < p.size(); i++)
        m[p[i]-'a']++;

    while(r < s.size()){
        if(m[s[r]-'a'] > 0){
            count--;
        }
        m[s[r]-'a']--;
        r++;

        if(count==0)
            ans.push_back(l);

        if(r-l==p.size()){
            if(m[s[l]-'a'] >= 0){
                count++;
            }
            m[s[l]-'a']++;
            l++;
        }
    }

    return ans;
}
