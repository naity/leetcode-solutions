# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        """
        Use a fast and slow pointer to find the middle node,
        and then reverse the seconde half, so that we can iterate through the first and reversed second half together to find the max sum

        Time: find middle: O(N), reverse: O(N), find max: O(N) => O(N)
        Space: O(1)
        """
        # use a sentinel node
        sentinel = ListNode(next=head)

        fast, slow = sentinel, sentinel

        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next

        # now slow.next points to the start of the second half
        second_curr = slow.next
        slow.next = None

        # reverse the second half
        prev = None
        while second_curr:
            nxt = second_curr.next
            second_curr.next = prev
            prev = second_curr
            second_curr = nxt

        # now find the max
        # prv is the head of the reversed second half
        p1, p2 = head, prev
        max_sum = 0
        while p1:
            max_sum = max(max_sum, p1.val + p2.val)
            p1 = p1.next
            p2 = p2.next

        return max_sum
