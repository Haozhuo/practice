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
    int minDepth(TreeNode* root) {
        //BFS
        if(root==nullptr)
            return 0;
        queue<TreeNode*> q;
        q.push(root);
        int depth = 1;

        while(!q.empty()){
            int size = q.size();

            while(size > 0){
                size--;
                TreeNode* temp = q.front(); q.pop();
                if(temp->left==nullptr && temp->right==nullptr)
                    return depth;
                if(temp->left!=nullptr)
                    q.push(temp->left);
                if(temp->right!=nullptr)
                    q.push(temp->right);
            }
            depth += 1;
        }

        return depth;
    }
};

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
    int minDepth(TreeNode* root) {
        //BFS
        if(root==nullptr)
            return 0;
        queue<vector<TreeNode*>> q;
        vector<TreeNode*> temp; temp.push_back(root);
        q.push(temp);
        int depth = 1;

        while(!q.empty()){
            temp = q.front(); q.pop();
            vector<TreeNode*> to_add;
            for(int i = 0; i < temp.size(); i++){
                if(temp[i]->left==nullptr && temp[i]->right==nullptr)
                    return depth;
                if(temp[i]->left!=nullptr)
                    to_add.push_back(temp[i]->left);
                if(temp[i]->right!=nullptr)
                    to_add.push_back(temp[i]->right);
            }
            q.push(to_add);
            depth += 1;
        }

        return depth;
    }
};
