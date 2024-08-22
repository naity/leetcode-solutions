# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(
        self, head: Optional[ListNode], left: int, right: int
    ) -> Optional[ListNode]:
        """
        1. locate the left node
        2. reverse [left, right] nodes
        3. reconnect nodes

        Time: O(N)
        Space: O(1)
        """

        sentinel = ListNode(next=head)

        # the node before left
        prev_left = None

        # pointer for current node
        curr = sentinel

        # step 1 - locate the left node
        for _ in range(left):
            prev_left = curr
            curr = curr.next

        # step2 - reverse
        prev = None
        for _ in range(left, right + 1):
            # next node
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp

        # step 3 - reconnect nodes
        # the curr pointer points to whatever the next pointer of the right node points to
        # the prev points to the right node
        # the prev_left.next points to the left node
        prev_left.next.next = curr
        prev_left.next = prev

        return sentinel.next
