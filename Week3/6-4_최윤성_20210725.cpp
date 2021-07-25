class Solution {
public:
    bool isPalindrome(ListNode* head) {
        list<int> l;
        list<int> rl;
        for(; head; head = head->next) {
            l.push_back(head->val);
            rl.push_front(head->val);
        }
        return l == rl;
    }
};