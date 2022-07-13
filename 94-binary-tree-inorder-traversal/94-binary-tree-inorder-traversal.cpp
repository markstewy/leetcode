/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    vector<int> inorderTraversal(TreeNode* root) {
        vector<int> v;
        inorderTarversalHelper(v, root);
        return v;
    }
    void inorderTarversalHelper(vector<int>& v, TreeNode* node) {
        if (node == nullptr) return;
        
        inorderTarversalHelper(v, node->left);
        v.push_back(node->val);
        inorderTarversalHelper(v, node->right);
    }
};