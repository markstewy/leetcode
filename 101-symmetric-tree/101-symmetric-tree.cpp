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
    bool isSymmetric(TreeNode* root) {
        bool result = true;
        isSymmetricHelper(root->left, root->right, result);
        return result;
    }
    
    void isSymmetricHelper(TreeNode* left, TreeNode* right, bool& result) {   
        // base
        if (left == nullptr || right == nullptr) {
            if (left != right) {
                result = false;
                return;
            } else {
                return;
            }
        } else if (left->val != right->val) {
            result = false;
            return;
        }
        
        // check child symmetry on both sides
        
        // Outer symmetry
        if (left->left == nullptr || right->right == nullptr) {
            if (left->left != right->right) {
                result = false;
                return;
            }
        } else if (left->left->val != right->right->val) {
            result = false;
            return;
        }
        
        // Inner symmetry
        if (left->right == nullptr || right->left == nullptr) {
            if (left->right != right->left) {
                result = false;
                return;
            }
        } else if (left->right->val != right->left->val) {
            result = false;
            return;
        }
        
        // symmetrical traversion
        TreeNode* outerLeft = left->left;
        TreeNode* outerRight= right->right;
        isSymmetricHelper(outerLeft, outerRight, result);
        
        TreeNode* innerLeft = left->right;
        TreeNode* innerRight = right->left;
        isSymmetricHelper(innerLeft, innerRight, result);
        
    }
};