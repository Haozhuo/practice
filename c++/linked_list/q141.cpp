bool hasCycle(ListNode *head) {
            if(head==nullptr || head->next == nullptr)
        return false;

    ListNode* slow = head;
    ListNode* fast = head->next;

    while(slow != fast){
        if(fast == nullptr || fast->next == nullptr)
            return false;
        fast = fast->next->next;
        slow = slow->next;
    }

    return true;
}
