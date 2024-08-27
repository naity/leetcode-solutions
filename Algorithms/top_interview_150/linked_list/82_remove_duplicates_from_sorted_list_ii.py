# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Use a prev pointer to remember the node before the duplicated numbers
        reconnect it to the node after the sequence

        Time: O(N) visit each node only once
        Space: O(1)
        """

        sentinel = ListNode()
        sentinel.next = head
        prev = sentinel
        curr = head

        while curr:
            # use a flag to indicate duplicates
            flag = False
            while curr.next and curr.val == curr.next.val:
                curr = curr.next
                # a bit repetitive, but okay
                flag = True

            if flag:
                # reconnect
                prev.next = curr.next
            else:
                prev = curr

            curr = curr.next

        return sentinel.next
