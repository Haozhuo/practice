#recursive approach
 /**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
TreeNode* buildTree(vector<int>& inorder, vector<int>& postorder) {
    return create(inorder,postorder,0,inorder.size()-1,0,postorder.size()-1);
}

TreeNode* create(vector<int>& inorder, vector<int>& postorder, int is, int ie, int ps, int pe){
    if(ps > pe || is > ie)
        return nullptr;

    TreeNode* root = new TreeNode(postorder[pe]);
    int pos = 0;
    for(int i = 0; i < inorder.size(); i++){
        if(inorder[i]==root->val){
            pos = i;
            break;
        }
    }

    root->left = create(inorder,postorder,is,pos-1,ps,ps+pos-is-1);
    root->right = create(inorder,postorder,pos+1,ie,pe-(ie-pos-1)-1,pe-1);

    return root;
}
