class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Use recursion
        reverse the rest, and then change its next's next to point to itself, and change its next pointer to None

        Time: O(N)
        Space: O(N)
        """

        if head is None or head.next is None:
            return head

        new_head = self.reverseList(head.next)

        head.next.next = head
        head.next = None

        return new_head
