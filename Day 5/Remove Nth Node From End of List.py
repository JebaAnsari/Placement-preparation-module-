class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        slow = fast = head
        
        for _ in range(n):
            fast = fast.next
        
        # if fast is null, then it implies that we must remove
        # the first node. Hence, we'll return the next node
        # (after the first node) as an answer.
        if not fast:
            return head.next
        
        while fast.next:
            slow = slow.next
            fast = fast.next
        
        slow.next = slow.next.next
        return head
