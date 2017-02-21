int numberOfBoomerangs(vector<pair<int, int>>& points) {
    int num = 0;
    for(int i = 0; i < points.size(); i++){
        unordered_map<int,int> um;
        for(int j = 0; j < points.size(); j++){
            int f = points[i].first - points[j].first;
            int s = points[i].second - points[j].second;
            um[f*f+s*s]++;
        }

        for(unordered_map<int,int>::iterator it = um.begin(); it != um.end(); it++)
            num += (it->second)*(it->second -1);
    }

    return num;
}
