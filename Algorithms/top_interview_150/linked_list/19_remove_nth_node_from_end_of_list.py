# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
        Suppose the length of the list is L
        the first half has L-n nodes, the second half has n nodes
        find the (L-n)th node can solve the problem.
        Can do two iterations, one to get L, the second to find L-n and delete the L-n+1 node
        Can solve with one pass by using two pointers
        let p1 start first and take n steps
        then p1, p2 move together until p1 reaches the end
        p2 will be at the L-n node

        Time: O(L)
        Space: O(1)
        """

        sentinel = ListNode(next=head)

        p1 = p2 = sentinel

        for _ in range(n):
            p1 = p1.next

        # note p1.next not p1, we want to stop at the last node so we take exactly L-n steps
        while p1.next:
            p1 = p1.next
            p2 = p2.next

        p2.next = p2.next.next

        return sentinel.next
