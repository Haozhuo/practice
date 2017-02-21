ListNode* mergeTwoLists(ListNode* l1, ListNode* l2) {
    ListNode* dummy = new ListNode(0);
    ListNode* curr = dummy;
    while(l1 != NULL && l2 != NULL){
        if(l1->val <= l2->val){
            curr->next = new ListNode(l1->val);
            l1 = l1->next;
        }
        else{
            curr->next = new ListNode(l2->val);
            l2 = l2->next;
        }

        curr = curr->next;
    }

    if(l1==NULL)
        curr->next = l2;
    if(l2==NULL)
        curr->next = l1;

    return dummy->next;
}
