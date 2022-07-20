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

    ListNode* mergeKLists(vector<ListNode*>& lists) {
        // flatten lists into single array
        vector<ListNode*> singleList;
        
        for (int i = 0; i < lists.size(); i++) {
            ListNode* head = lists[i];
            while(head) {
                singleList.push_back(head);
                head = head->next;
            }
        }
        
        // sort the flattened list
        std::sort(singleList.begin(), singleList.end(), 
                  [](ListNode*& a, ListNode*& b) { 
                              return a->val < b->val; 
                    });
        
         if (singleList.size() <= 0) {
            return nullptr;
         }
        
        ListNode* root = singleList[0];
        // re link the nodes as ordered in the array
        for (int i = 0; i < singleList.size() - 1; i++) {
            singleList[i]->next = singleList[i + 1];
        }
        singleList[singleList.size() - 1]->next = nullptr;
        
        return root;
    }
    

};