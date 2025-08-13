# Leetcode 2059: Minimum Operations to Convert Number
# https://leetcode.com/problems/minimum-operations-to-convert-number/
# Solved on 13th of August, 2025
from collections import deque


class Solution:
    def minimumOperations(self, nums: list[int], start: int, goal: int) -> int:
        """
        Calculates the minimum number of operations to transform 'start' into 'goal'.
        Operations include addition, subtraction, and XOR with any number from 'nums'.
        :param nums: A list of integers to use in operations.
        :param start: The initial integer.
        :param goal: The target integer.
        :return: The minimum number of operations, or -1 if 'goal' is unreachable.
        """
        if start == goal:
            return 0

        MAX_VAL = 1000
        visited = [False] * (MAX_VAL + 1)
        q = deque()
        # Only enqueue start if it's inside the allowed range
        if 0 <= start <= MAX_VAL:
            q.append((start, 0))
            visited[start] = True
        else:
            # Per constraints start is within range, but guard anyway
            q.append((start, 0))

        while q:
            x, steps = q.popleft()
            for num in nums:
                # Three operations
                for y in (x + num, x - num, x ^ num):
                    if y == goal:
                        return steps + 1
                    # Only enqueue further states if within allowed range and not seen
                    if 0 <= y <= MAX_VAL and not visited[y]:
                        visited[y] = True
                        q.append((y, steps + 1))

        return -1