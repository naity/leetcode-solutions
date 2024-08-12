# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        """
        Iterate over the two linked lists and keep track the carry
        Check carry after the iteration, add node if needed

        Time: O(max(M, N))
        Space: O(max(M, N))
        """
        # use a sentinel node
        sentinel = ListNode()
        curr = sentinel
        carry = 0

        p1 = l1
        p2 = l2
        while p1 or p2:
            total = carry
            if p1:
                total += p1.val
                p1 = p1.next
            if p2:
                total += p2.val
                p2 = p2.next

            carry = total // 10
            val = total % 10

            # new node and advance curr
            curr.next = ListNode(val=val)
            curr = curr.next

        # in case need to add an extra node
        if carry == 1:
            curr.next = ListNode(val=1)

        return sentinel.next
