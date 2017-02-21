bool isStrobogrammatic(string num) {
    unordered_map<char,char> us{{'0','0'},{'1','1'},{'8','8'},{'6','9'},{'9','6'}};
    int s = 0;
    int e = num.size() - 1;
    while(s <= e){
        if(us.find(num[s])==us.end() || us.find(num[s])->second != num[e])
            return false;
        s++;
        e--;
    }

    return true;
}
