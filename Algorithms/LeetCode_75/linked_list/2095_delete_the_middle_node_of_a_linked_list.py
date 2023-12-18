class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        To determine the list length, one need to traverse the entire list, which takes O(N) time.
        However, if we use two pointers, pfast moves 2 steps while pslow moves one step. When pfast reaches the end, pslow will piont to the middle.
        pslow actually needs to point to the previous node of the middle, we move pfast only if both pfast.next and pfast.next.next is not None

        Time: O(N)
        Space: O(1)
        """

        sentinel = ListNode(next=head)

        p_slow, p_fast = sentinel, sentinel

        while p_fast and p_fast.next and p_fast.next.next:
            p_fast = p_fast.next.next
            p_slow = p_slow.next

        # p_slow points to the previous node of middle
        p_slow.next = p_slow.next.next

        return sentinel.next
