/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    bool isPalindrome(ListNode* head) {
        if(head == nullptr || head->next == nullptr){
            return true;
        }

        ListNode* fast = head; ListNode* slow = head;
        while(fast != nullptr && fast->next != nullptr){
            slow = slow->next;
            fast = fast->next->next;
        }


        if(fast)
            slow = slow->next;

        slow = reverseList(slow);

        while(slow != nullptr){
            if(head->val != slow->val)
                return false;
            head = head->next;
            slow = slow->next;
        }

        return true;
    }
private:
    ListNode* reverseList(ListNode* node){
        ListNode* prev = node;
        ListNode* curr = node->next;
        prev->next = nullptr;

        while(curr != nullptr){
            ListNode* temp = curr->next;
            curr->next = prev;
            prev = curr;
            curr = temp;
        }

        return prev;
    }
};
