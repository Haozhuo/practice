vector<vector<int>> verticalOrder(TreeNode* root) {
    vector<vector<int>> res;
    if(!root)
        return res;

    map<int,vector<int>> um;
    queue<pair<TreeNode*,int>> q;
    q.push(make_pair(root,0));

    while(q.size()){
        TreeNode* front_node = q.front().first;
        int pos = q.front().second;
        q.pop();
        um[pos].push_back(front_node->val);

        if(front_node->left)
            q.push(make_pair(front_node->left,pos-1));
        if(front_node->right)
            q.push(make_pair(front_node->right,pos+1));
    }

    for(auto unit: um)
        res.push_back(unit.second);

    return res;
}
