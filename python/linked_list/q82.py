ListNode* deleteDuplicates(ListNode* head) {
    if(head==nullptr || head->next == nullptr)
        return head;
    ListNode* dummy = nullptr;
    if(head->val == 0)
        dummy = new ListNode(1);
    else
        dummy = new ListNode(0);
    dummy->next = head;
    ListNode* prev = dummy; ListNode* curr = head;
    while(curr!= nullptr){
        while(curr->next != nullptr && curr->val == curr->next->val)
            curr = curr->next;

        if(prev->next==curr)
            prev = curr;
        else
            prev->next = curr->next;

        curr = curr->next;
    }

    return dummy->next;
}
