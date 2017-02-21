/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    vector<vector<int>> levelOrder(TreeNode* root) {
        vector<vector<int>> ret;
        if(root==nullptr)
            return ret;
        queue<TreeNode*> q;
        q.push(root);

        while(!q.empty()){
            TreeNode* temp = nullptr;
            int size = q.size();
            vector<int> unit;

            //NOTE:the technique to use so that we do not have to use a vector to store all TreeNode
            //at a given level
            while(size > 0){
                temp = q.front(); q.pop();
                size--;
                if(temp->left!=nullptr)
                    q.push(temp->left);

                if(temp->right!=nullptr)
                    q.push(temp->right);

                unit.push_back(temp->val);
            }
            ret.push_back(unit);
        }

        return ret;
    }
};
