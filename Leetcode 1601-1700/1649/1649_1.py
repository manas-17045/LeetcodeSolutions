# Leetcode 1649: Create Sorted Array through Instructions
# https://leetcode.com/problems/create-sorted-array-through-instructions/
# Solved on 26th of July, 2025
class Solution:
    def createSortedArray(self, instructions: list[int]) -> int:
        """
        Calculates the minimum cost to create a sorted array from a given list of instructions.

        Args:
            instructions (list[int]): A list of integers representing the numbers to be inserted.
        Returns:
            int: The minimum cost to create the sorted array, modulo 10^9 + 7.
        """
        modValue = 10 ** 9 + 7
        size = 100002
        fenwickTree = [0] * size

        def update(index: int, value: int):
            while index < size:
                fenwickTree[index] += value
                index += index & (-index)

        def query(index: int) -> int:
            total = 0
            while index > 0:
                total += fenwickTree[index]
                index -= index & (-index)
            return total

        totalCost = 0
        for i, num in enumerate(instructions):
            countLess = query(num - 1)
            countGreater = i - query(num)

            cost = min(countLess, countGreater)
            totalCost = (totalCost + cost) % modValue

            update(num, 1)

        return totalCost