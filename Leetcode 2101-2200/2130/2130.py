# Leetcode 2130: Maximum Twin Sum of Linked List
# https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/
# Solved on 14th of June, 2026
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        """
        Calculates the maximum twin sum of a linked list of even length.

        :param head: Optional[ListNode], the head of the linked list.
        :return: int, the maximum twin sum found.
        """
        slowPointer = head
        fastPointer = head

        while fastPointer and fastPointer.next:
            slowPointer = slowPointer.next
            fastPointer = fastPointer.next.next

        prevNode = None
        currentNode = slowPointer
        while currentNode:
            nextNode = currentNode.next
            currentNode.next = prevNode
            prevNode = currentNode
            currentNode = nextNode

        firstHalf = head
        secondHalf = prevNode
        maxTwinSum = 0

        while secondHalf:
            currentTwinSum = firstHalf.val + secondHalf.val
            if currentTwinSum > maxTwinSum:
                maxTwinSum = currentTwinSum
            firstHalf = firstHalf.next
            secondHalf = secondHalf.next

        return maxTwinSum