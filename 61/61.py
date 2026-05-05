# Leetcode 61: Rotate List
# https://leetcode.com/problems/rotate-list/
# Solved on 5th of May, 2026
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        """
        Rotates the linked list to the right by k places.

        :param head: The head of the singly-linked list.
        :param k: The number of positions to rotate the list to the right.
        :return: The new head of the rotated linked list.
        """
        if not head or not head.next or k == 0:
            return head

        listLength = 1
        currentTail = head

        while currentTail.next:
            currentTail = currentTail.next
            listLength += 1

        effectiveRotations = k % listLength

        if effectiveRotations == 0:
            return head

        currentTail.next = head

        stepsToNewTail = listLength - effectiveRotations
        newTail = head

        for _ in range(stepsToNewTail - 1):
            newTail = newTail.next

        newHead = newTail.next
        newTail.next = None

        return newHead