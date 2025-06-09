# Leetcode 3462: Maximum Sum With at Most K Elements
# https://leetcode.com/problems/maximum-sum-with-at-most-k-elemts/
# Solved on 9th of June, 2025

class Solution:
    def maxSum(self, grid: list[list[int]], limit: list[int], k: int):
        """
        Calculates the maximum sum of k elements from a grid, with a limit on how many elements can be taken from each row.

        Args:
            grid: A 2D list of integers representing the grid.
            limit: A list of integers where limit[i] is the maximum number of elements that can be taken from row i.
            k: The total number of elements to select.

        Returns:
            The maximum possible sum of k elements satisfying the row limits.
        """
        # Flatten all elements into (value, row_index)
        items = []
        for i, row in enumerate(grid):
            for v in row:
                items.append((v, i))

        # Sort descending by value
        items.sort(key=lambda x: x[0], reverse=True)

        # How many taken from each row
        taken = [0] * len(grid)
        total = 0
        cnt = 0

        # Greedily take the next-largest item if its row still has capacity
        for v, i in items:
            if cnt >= k:
                break

            if taken[i] < limit[i]:
                total += v
                taken[i] += 1
                cnt += 1

        return total