ListNode* removeNthFromEnd(ListNode* head, int n) {
    ListNode* dummy = new ListNode(0);
    dummy->next = head;
    ListNode* f = dummy; ListNode* s = dummy;

    for(int i = 0; i <= n; i++)
        f = f->next;

    while(f != nullptr){
        f = f->next;
        s = s->next;
    }

    ListNode* temp = s->next;
    s->next = s->next->next;
    delete temp;
    return dummy->next;
}
