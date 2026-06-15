# Leetcode 2095: Delete the Middle Node of a Linked List
# https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list/
# Solved on 15th of June, 2026
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Deletes the middle node of a linked list and returns the head of the modified list.

        :param head: Optional[ListNode] - The head of the linked list.
        :return: Optional[ListNode] - The head of the linked list after deleting the middle node.
        """
        if not head or not head.next:
            return None

        slowPtr = head
        fastPtr = head
        prevPtr = None

        while fastPtr and fastPtr.next:
            prevPtr = slowPtr
            slowPtr = slowPtr.next
            fastPtr = fastPtr.next.next

        prevPtr.next = slowPtr.next
        return head