# Leetcode 1649: Create Sorted Array through Instructions
# https://leetcode.com/problems/create-sorted-array-through-instructions/
# Solved on 26th of July, 2025
class Solution:
    def createSortedArray(self, instructions: list[int]) -> int:
        """
        Calculates the minimum cost to create a sorted array from a given list of instructions.
        The cost of inserting an element is the minimum of the number of elements already in the array
        that are strictly less than it, and the number of elements strictly greater than it.
        :param instructions: A list of integers representing the elements to be inserted.
        :return: The minimum total cost to create the sorted array, modulo 10^9 + 7.
        """
        MOD = 10 ** 9 + 7

        # Binary Indexed Tree (1-indexed)
        max_val = max(instructions)
        bit = [0] * (max_val + 2)

        def update(i: int) -> None:
            while i < len(bit):
                bit[i] += 1
                i += i & -i

        def query(i: int) -> int:
            s = 0
            while i > 0:
                s += bit[i]
                i -= i & -i
            return s

        cost = 0
        processed = 0

        for x in instructions:
            # Number of existing elements < x
            less = query(x - 1)
            # Number of existing elements > x
            greater = processed - query(x)

            cost = (cost + min(less, greater)) % MOD

            # Insert x into BIT
            update(x)
            processed += 1

        return cost