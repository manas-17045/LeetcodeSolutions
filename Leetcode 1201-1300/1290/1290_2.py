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
        Converts a binary number represented by a linked list to its decimal integer value.
        :param head: The head of the linked list representing the binary number.
        :return: The decimal integer value of the binary number.
        """
        num = 0
        curr = head
        # At each step, shift existing bits left and add the new bit
        while curr:
            num = (num << 1) | curr.val
            curr = curr.next
        return num