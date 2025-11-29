# Leetcode 3690: Split and Merge Array Transformation
# https://leetcode.com/problems/split-and-merge-array-transformation/
# Solved on 29th of November, 2025
from collections import deque


class Solution:
    def minSplitMerge(self, nums1: list[int], nums2: list[int]) -> int:
        """
        Calculates the minimum number of split and merge operations to transform nums1 into nums2.

        Args:
            nums1 (list[int]): The starting array.
            nums2 (list[int]): The target array.
        Returns:
            int: The minimum number of operations, or -1 if transformation is not possible.
        """
        startState = tuple(nums1)
        targetState = tuple(nums2)

        if startState == targetState:
            return 0

        queue = deque([(startState, 0)])
        visited = {startState}
        n = len(nums1)

        while queue:
            currentState, currentDist = queue.popleft()

            for i in range(n):
                for j in range(i + 1, n + 1):
                    subArray = currentState[i:j]
                    remainingArray = currentState[:i] + currentState[j:]

                    for k in range(len(remainingArray) + 1):
                        nextState = remainingArray[:k] + subArray + remainingArray[k:]

                        if nextState == targetState:
                            return currentDist + 1

                        if nextState not in visited:
                            visited.add(nextState)
                            queue.append((nextState, currentDist + 1))

        return -1