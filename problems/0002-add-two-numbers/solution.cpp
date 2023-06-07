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
        ListNode* head_ptr = new ListNode();
        ListNode* tail_ptr = head_ptr;
        int carry = 0;

        do {

            int l1_val = l1 == nullptr ? 0 : l1->val;
            int l2_val = l2 == nullptr ? 0 : l2->val;

            int sum = l1_val + l2_val + carry;
            tail_ptr->val = sum % 10;
            carry = sum > 9 ? 1 : 0;

            bool l1_has_next = (l1 != nullptr && l1->next != nullptr);
            bool l2_has_next = (l2 != nullptr && l2->next != nullptr);

            if (l1_has_next || l2_has_next || carry > 0) {
                tail_ptr->next = new ListNode();
                tail_ptr = tail_ptr->next;

                l1 = l1 == nullptr ? nullptr : l1->next;
                l2 = l2 == nullptr ? nullptr : l2->next;
            } else {
                return head_ptr;
            }

        } while (true);
    }
};
