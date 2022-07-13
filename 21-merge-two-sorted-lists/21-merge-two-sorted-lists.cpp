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
    ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {
        ListNode* c1 = list1;
        ListNode* c2 = list2;
        ListNode* lne = nullptr; // list new end
        ListNode* lnh = nullptr; // list new head
        // catch nullptr parmeters
        if (!c1) {
            return c2;
        }
        
        if (!c2) {
            return c1;
        }
        
        // get initial head node of new list
         if (c1->val < c2->val) {
             lne = c1;
             lnh = c1;
             c1 = c1->next;
         } else {
             lne = c2;
             lnh = c2;
             c2 = c2->next;
         }
        
        while(c1 && c2) {
            // append and increment current
            if (c1->val < c2->val) {
                lne->next = c1;
                lne = lne->next;
                c1 = c1->next;
            } else {
                lne->next = c2;
                lne = lne->next;
                c2 = c2->next;
            }
        } 
        // append remainder of other list
        if (c1) {
            lne->next = c1;
        }
        if (c2) {
            lne->next = c2;
        }
        return lnh;
    }
};