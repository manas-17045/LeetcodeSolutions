# Leetcode 1306: Jump Game III
# https://leetcode.com/problems/jump-game-iii/
# Solved on 31st of August, 2025
from collections import deque


class Solution:
    def canReach(self, arr: list[int], start: int) -> bool:
        """
        Determines if it's possible to reach an index with value 0 from a given start index.

        :param arr: A list of non-negative integers where arr[i] is the maximum jump length from index i.
        :param start: The starting index.
        :return: True if an index with value 0 can be reached, False otherwise.
        """
        n = len(arr)
        q = deque([start])

        while q:
            i = q.popleft()
            # If already visited, skip
            if arr[i] == -1:
                continue
            # If we've reached a zero, success
            if arr[i] == 0:
                return True

            jump = arr[i]
            # Mark visited
            arr[i] = -1

            # Neighbors
            left = i - jump
            right = i + jump

            if 0 <= left < n and arr[left] != -1:
                q.append(left)

            if 0 <= right < n and arr[right] != -1:
                q.append(right)

        return False