# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        """
        Fast and slow pointers, if there is a cycle,
        the two pointers will meet as
        if there is a cycle, suppose when slow reaches the cycle start,
        fast is x steps ahead, we can also think is as fast is L - x behind,
        where L is the length of the cycle, each time, the distance betwee the
        two pointers reduce by 1, and after L-x steps, they will meet.
        note that L-x is at most L

        Time: O(N), as it takes the slow pointer N-L time to get to the cycle start,
        and it takes at most l for they meet if there is a cycle
        Space: O(1)
        """

        p1, p2 = head, head

        while p1 is not None and p1.next is not None:
            p1 = p1.next.next
            p2 = p2.next

            if p1 == p2:
                return True

        return False
