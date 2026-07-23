from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(
        self,
        head: Optional[ListNode],
        n: int
    ) -> Optional[ListNode]:

        dummy = ListNode(0, head)

        slow = dummy
        fast = dummy

        # Move fast n + 1 positions ahead
        for _ in range(n + 1):
            fast = fast.next

        # Move both pointers until fast reaches the end
        while fast is not None:
            slow = slow.next
            fast = fast.next

        # slow is immediately before the node to remove
        slow.next = slow.next.next

        return dummy.next