int fourSumCount(vector<int>& A, vector<int>& B, vector<int>& C, vector<int>& D) {
    unordered_map<int,int> um;
    int ret = 0;
    for(int i = 0; i < A.size(); i++){
        for(int j = 0; j < B.size(); j++){
            um[A[i]+B[j]]++;
        }
    }

    for(int i = 0; i < C.size(); i++){
        for(int j = 0; j < D.size(); j++){
            unordered_map<int,int>::iterator umi = um.find(-C[i]-D[j]);
            if(umi != um.end())
                ret += umi->second;
        }
    }

    return ret;
}
