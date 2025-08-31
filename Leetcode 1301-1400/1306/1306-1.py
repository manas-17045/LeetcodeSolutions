# Leetcode 1306: Jump Game III
# https://leetcode.com/problems/jump-game-iii/
# Solved on 31st of August, 2025
import collections


class Solution:
    def canReach(self, arr: list[int], start: int) -> bool:
        """
        Determines if it's possible to reach an index with value 0 in the array.

        Args:
            arr (list[int]): The array of non-negative integers.
            start (int): The starting index.
        Returns:
            bool: True if an index with value 0 can be reached, False otherwise.
        """
        arrayLength = len(arr)
        queue = collections.deque([start])
        visited = {start}

        while queue:
            currentIndex = queue.popleft()

            if arr[currentIndex] == 0:
                return True

            jumpValue = arr[currentIndex]

            forwardIndex = currentIndex + jumpValue
            if 0 <= forwardIndex < arrayLength and forwardIndex not in visited:
                visited.add(forwardIndex)
                queue.append(forwardIndex)

            backwardIndex = currentIndex - jumpValue
            if 0 <= backwardIndex < arrayLength and backwardIndex not in visited:
                visited.add(backwardIndex)
                queue.append(backwardIndex)

        return False