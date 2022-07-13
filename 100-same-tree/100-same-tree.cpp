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
    bool isSameTree(TreeNode* p, TreeNode* q) {
        bool result = true;
        isSameTreeHelper(p, q, result);
        return result;
    }
    
    void isSameTreeHelper(TreeNode* p, TreeNode* q, bool& result) {
        if (p == nullptr || q == nullptr) { 
            if (p != q) { result = false; }
            return; 
        }
        
        isSameTreeHelper(p->left, q->left, result);
        if (p->val != q->val) { result = false; }
        isSameTreeHelper(p->right, q->right, result);
    }
};