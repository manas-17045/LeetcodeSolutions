# Leetcode 2816: Double a Number Represented as a Linked List
# https://leetcode.com/problems/double-a-number-represented-as-a-linked-list/
# Solved on 7th of January, 2026
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Doubles the number represented by a linked list.

        :param head: The head of the linked list representing the number.
        :return: The head of the linked list representing the doubled number.
        """
        if head.val > 4:
            head = ListNode(0, head)

        current = head
        while current:
            current.val = (current.val * 2) % 10
            if current.next and current.next.val > 4:
                current.val += 1
            current = current.next

        return head