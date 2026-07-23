from typing import List, Optional
import heapq


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(
        self,
        lists: List[Optional[ListNode]]
    ) -> Optional[ListNode]:

        min_heap = []

        # Add the first node of every non-empty list
        for index, node in enumerate(lists):
            if node is not None:
                heapq.heappush(min_heap, (node.val, index, node))

        dummy = ListNode()
        current = dummy

        while min_heap:
            value, index, node = heapq.heappop(min_heap)

            current.next = node
            current = current.next

            if node.next is not None:
                heapq.heappush(
                    min_heap,
                    (node.next.val, index, node.next)
                )

        return dummy.next