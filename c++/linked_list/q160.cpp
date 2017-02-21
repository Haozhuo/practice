ListNode *getIntersectionNode(ListNode *headA, ListNode *headB) {
    if(headA==nullptr || headB == nullptr)
        return nullptr;
    ListNode* p1 = headA;
    ListNode* p2 = headB;

    while(p1!=NULL&&p2!=NULL&&p1!=p2){
        p1 = p1->next;
        p2 = p2->next;

        if(p1==p2)
            return p1;
        if(p1==NULL)
            p1 = headB;
        if(p2==NULL)
            p2 = headA;
    }

    return p1;
}

ListNode *getIntersectionNode2(ListNode *headA, ListNode *headB) {
        if(headA==nullptr || headB == nullptr)
            return nullptr;
        ListNode* l1 = headA;
        ListNode* l2 = headB;

        bool l1hit = false;
        bool l2hit = false;

        while(true){
            if(l1==nullptr){
                if(!l1hit){
                    l1hit = true;
                    l1 = headB;
                }
                else
                    return nullptr;
            }
            if(l2==nullptr){
                if(!l2hit){
                    l2hit = true;
                    l2 = headA;
                }
                else
                    return nullptr;
            }

            if(l1==l2)
                return l1;

            l1 = l1->next;
            l2 = l2->next;
        }

        return nullptr;
    }
