class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        need to track the end of odd, and then connect it to the head of even

        Time: O(N)
        Space: O(1)
        """

        if head is None or head.next is None:
            return head

        curr_odd, curr_even = head, head.next
        head_even = curr_even

        while curr_even and curr_even.next:
            curr_odd.next = curr_even.next
            curr_even.next = curr_even.next.next
            curr_odd = curr_odd.next
            curr_even = curr_even.next

        # connect
        curr_odd.next = head_even

        return head
