# Leetcode 1386: Cinema Seat Allocation
# https://leetcode.com/problems/cinema-seat-allocation/
# Solved on 19th of August, 2026
from collections import defaultdict


class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: list[list[int]]) -> int:
        """
        Calculates the maximum number of 4-person families that can be seated together.

        Valid 4-person allocations in a 10-seat row are seats (2, 3, 4, 5), 
        (6, 7, 8, 9), or (4, 5, 6, 7).

        Parameters:
            n (int): Total number of rows in the cinema.
            reservedSeats (List[List[int]]): 2D list of [row, col] pairs representing booked seats.

        Returns:
            int: Maximum number of 4-person family groups that can be accommodated.
        """
        reservedMap = defaultdict(int)

        for row, seat in reservedSeats:
            if 2 <= seat <= 9:
                reservedMap[row] |= (1 << seat)

        totalGroups = (n - len(reservedMap)) * 2

        leftM = (1 << 2) | (1 << 3) | (1 << 4) | (1 << 5)
        rightM = (1 << 6) | (1 << 7) | (1 << 8) | (1 << 9)
        midM = (1 << 4) | (1 << 5) | (1 << 6) | (1 << 7)

        for rowM in reservedMap.values():
            canL = (rowM & leftM) == 0
            canR = (rowM & rightM) == 0
            
            if canL and canR:
                totalGroups += 2
            elif canL or canR or ((rowM & midM) == 0):
                totalGroups += 1

        return totalGroups