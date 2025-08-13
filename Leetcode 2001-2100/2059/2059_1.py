# Leetcode 2059: Minimum Operations to Convert Number
# https://leetcode.com/problems/minimum-operations-to-convert-number/
# Solved on 13th of August, 2025
import collections


class Solution:
    def minimumOperations(self, nums: list[int], start: int, goal: int) -> int:
        """
        Calculates the minimum number of operations to convert 'start' to 'goal'.

        Args:
            nums (list[int]): A list of integers to be used in operations.
            start (int): The starting integer.
            goal (int): The target integer.
        """

        queue = collections.deque([(start, 0)])
        visited = {start}

        while queue:
            currentValue, currentOps = queue.popleft()

            for num in nums:
                # List of possible next values from the three operations
                nextValues = [
                    currentValue + num,
                    currentValue - num,
                    currentValue ^ num
                ]

                for nextValue in nextValues:
                    # Check if the goal is reached
                    if nextValue == goal:
                        return currentOps + 1

                    # Check if the next value is a valid state for further operations
                    if 0 <= nextValue <= 1000 and nextValue not in visited:
                        visited.add(nextValue)
                        queue.append((nextValue, currentOps + 1))

        return -1