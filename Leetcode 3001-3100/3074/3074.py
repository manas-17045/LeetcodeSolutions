# Leetcode 3074: Apple Redistribution into Boxes
# https://leetcode.com/problems/apple-redistribution-into-boxes/
# Solved on 24th of December, 2025
class Solution:
    def minimumBoxes(self, apple: list[int], capacity: list[int]) -> int:
        """
        Calculates the minimum number of boxes required to redistribute all apples.

        Args:
            apple (list[int]): A list of integers representing the number of apples in each basket.
            capacity (list[int]): A list of integers representing the capacity of each box.

        Returns:
            int: The minimum number of boxes needed.
        """
        totalApples = sum(apple)
        capacity.sort(reverse=True)
        currentCapacity = 0

        for i, cap in enumerate(capacity):
            currentCapacity += cap

            if currentCapacity >= totalApples:
                return i + 1

        return len(capacity)