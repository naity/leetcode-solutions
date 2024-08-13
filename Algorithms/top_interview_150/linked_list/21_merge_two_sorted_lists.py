# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        """
        Iterate over the two lists, set the next pointer to the one with a smaller value

        Worse case visit all nodes in list1 and list2, e.g. [1, 2, 3, 10] and [4, 5, 6]
        Time: O(M+N)
        Space: O(1)
        """

        sentinel = ListNode()

        curr = sentinel
        p1, p2 = list1, list2

        while p1 and p2:
            # compare value
            if p1.val <= p2.val:
                curr.next = p1
                p1 = p1.next
            else:
                curr.next = p2
                p2 = p2.next

            # move curr
            curr = curr.next

        # check which one has left nodes
        if p1:
            curr.next = p1
        else:
            curr.next = p2

        return sentinel.next
