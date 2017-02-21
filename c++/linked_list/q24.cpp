ListNode* swapPairs(ListNode* head) {
     ListNode* dummy = new ListNode(0);
     dummy->next = head;
     ListNode* curr = dummy;
     while(curr->next != nullptr && curr->next->next != nullptr){
         ListNode* f = curr->next;
         ListNode* s = curr->next->next;

         f->next = s->next;
         s->next = f;
         curr->next = s;
         curr = curr->next->next;
     }

     return dummy->next;
 }
