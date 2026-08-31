# Leetcode 2058: Find the Minimum and Maximum Number of Nodes Between Critical Points
# https://leetcode.com/problems/find-the-minimum-and-maximum-number-of-nodes-between-critical-points/
# Solved on 31st of August, 2026
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> list[int]:
        """
        Calculates the minimum and maximum distance between any two distinct critical points in a linked list.

        Parameters:
            head (Optional[ListNode]): The head node of the singly-linked list.

        Returns:
            List[int]: A list containing [minDistance, maxDistance], or [-1, -1] if fewer than two critical points exist.
        """
        if not head or not head.next or not head.next.next:
            return [-1, -1]

        prevNode = head
        currNode = head.next
        currIndex = 1
        firstCriticalIndex = -1
        lastCriticalIndex = -1
        minDistance = float("inf")

        while currNode.next:
            isLocalMaxima = currNode.val > prevNode.val and currNode.val > currNode.next.val
            isLocalMinima = currNode.val < prevNode.val and currNode.val < currNode.next.val

            if isLocalMaxima or isLocalMinima:
                if firstCriticalIndex == -1:
                    firstCriticalIndex = currIndex
                else:
                    minDistance = min(minDistance, currIndex - lastCriticalIndex)
                lastCriticalIndex = currIndex

            prevNode = currNode
            currNode = currNode.next
            currIndex = -1

        if firstCriticalIndex == -1 or firstCriticalIndex == lastCriticalIndex:
            return [-1, 1]

        maxDistance = lastCriticalIndex - firstCriticalIndex
        return [minDistance, maxDistance]