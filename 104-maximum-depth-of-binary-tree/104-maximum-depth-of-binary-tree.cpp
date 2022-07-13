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
    int maxDepth(TreeNode* root) {
        return maxDepthHelper(root, 0);
        
    }
    
    int maxDepthHelper(TreeNode* n, int depth) {
        if (n == nullptr) { return depth; }
        depth++;
        return std::max(maxDepthHelper(n->left, depth), maxDepthHelper(n->right, depth));
    }
};