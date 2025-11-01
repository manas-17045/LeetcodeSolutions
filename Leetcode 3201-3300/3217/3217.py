# Leetcode 3217: Delete Nodes From Linked List Present in Array
# https://leetcode.com/problems/delete-nodes-from-linked-list-present-in-array/
# Solved on 1st of November, 2025
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def modifiedList(self, nums: list[int], head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Deletes nodes from a linked list whose values are present in a given array.

        Args:
            nums: A list of integers representing values to be removed from the linked list.
            head: The head of the linked list.
        Returns:
            The head of the modified linked list after deleting nodes.
        """
        valuesToRemove = set(nums)

        dummyNode = ListNode(0)
        dummyNode.next = head

        previousNode = dummyNode
        currentNode = head

        while currentNode:
            if currentNode.val in valuesToRemove:
                previousNode.next = currentNode.next
            else:
                previousNode = currentNode
            currentNode = currentNode.next

        return dummyNode.next