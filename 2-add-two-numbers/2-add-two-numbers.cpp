/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        int sum = l1->val + l2->val;
        int carry = 0;
        
        if ( sum > 9) {
            carry = 1;
            sum %= 10;
        }
        ListNode* solution = new ListNode(sum);
        ListNode* solutionHead = solution;
        l1 = l1->next;
        l2 = l2->next;
        
        while (l1 || l2) {
                int v1 = l1 ? l1->val : 0;
                int v2 = l2 ? l2->val : 0;
                int sum = v1 + v2 + carry;
                if ( sum > 9) {
                    carry = 1;
                    sum %= 10;
                 } else {
                    carry = 0;
                }
                solution->next = new ListNode(sum);
                l1 = l1 ? l1->next : nullptr;
                l2 = l2 ? l2->next : nullptr;
                solution = solution->next;
        }
        if (carry) {
            solution->next = new ListNode(carry);
        }
        return solutionHead;
    }
};