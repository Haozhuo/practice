/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
ListNode* reverseList(ListNode* head) {
    if(head==nullptr || head->next==nullptr)
        return head;
    ListNode* prev = head;
    ListNode* curr = head->next;
    head->next = nullptr;

    while(curr != nullptr){
        ListNode* temp = curr->next;
        curr->next = prev;
        prev = curr;
        curr = temp;
    }

    return prev;
}
