# Leetcode 1290: Convert Binary Number in a Linked List to Integer
# https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer/
# Solved on 14th of July, 2025
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        """
        Given `head` which is a reference to the head of a singly-linked list.
        The list represents a binary number, convert it to an integer.

        Args:
            head (Optional[ListNode]): The head of the linked list representing the binary number.
        Returns:
            int: The decimal value of the binary number.
        """
        decimalValue = 0
        currentNode = head
        while currentNode:
            decimalValue = (decimalValue << 1) | currentNode.val
            currentNode = currentNode.next
        return decimalValue