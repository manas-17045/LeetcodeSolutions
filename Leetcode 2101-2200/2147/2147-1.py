# Leetcode 2147: Number of Ways to Divide a Long Corridor
# https://leetcode.com/problems/number-of-ways-to-divide-a-long-corridor/
# Solved on 6th of September, 2025
class Solution:
    def numberOfWays(self, corridor: str) -> int:
        """
        Calculates the number of ways to divide a long corridor.

        Args:
            corridor (str): A string representing the corridor, consisting of 'S' (seat) and 'P' (plant).
        Returns:
            int: The number of ways to divide the corridor, modulo 1,000,000,007.
        """
        mod = 1_000_000_007
        seatIndices = []
        for i in range(len(corridor)):
            if corridor[i] == 'S':
                seatIndices.append(i)

        numSeats = len(seatIndices)
        if numSeats == 0 or numSeats % 2 != 0:
            return 0

        waysToDivide = 1
        for i in range(1, numSeats - 1, 2):
            gap = seatIndices[i + 1] - seatIndices[i]
            waysToDivide = (waysToDivide * gap) % mod

        return waysToDivide