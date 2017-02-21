/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
    ListNode* dummy = new ListNode(0);
    dummy->next = nullptr;
    ListNode* l = dummy;
    int carry = 0;

    while(l1 != nullptr || l2 != nullptr){
        int n1 = 0; int n2 = 0;
        if(l1 != nullptr)
            n1 = l1->val;
        if(l2 != nullptr)
            n2 = l2->val;
        int sum = n1 + n2 + carry;
        carry = sum / 10;
        sum -= carry * 10;

        l->next = new ListNode(sum);
        l = l->next;
        if(l1 != nullptr)
            l1 = l1->next;
        if(l2 != nullptr)
            l2 = l2->next;
    }

    if(carry == 1)
        l->next = new ListNode(carry);

    return dummy->next;
}
