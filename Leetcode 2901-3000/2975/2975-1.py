# Leetcode 2975: Maximum Square Area by Removing Fences From a Field
# https://leetcode.com/problems/maximum-square-area-by-removing-fences-from-a-field/
# Solved on 20th of October, 2025
class Solution:
    def maximizeSquareArea(self, m: int, n: int, hFences: list[int], vFences: list[int]) -> int:
        """
        Calculates the maximum possible square area that can be formed by removing fences.

        Args:
            m (int): The height of the field.
            n (int): The width of the field.
            hFences (list[int]): A list of integers representing the positions of horizontal fences.
            vFences (list[int]): A list of integers representing the positions of vertical fences.

        Returns:
            int: The maximum possible square area, or -1 if no square can be formed.
        """

        hBoundaries = [1, m] + hFences
        vBoundaries = [1, n] + vFences

        hSideLengths = set()
        for i in range(len(hBoundaries)):
            for j in range(i + 1, len(hBoundaries)):
                diff = abs(hBoundaries[i] - hBoundaries[j])
                hSideLengths.add(diff)

        maxSide = 0

        for i in range(len(vBoundaries)):
            for j in range(i + 1, len(vBoundaries)):
                diff = abs(vBoundaries[i] - vBoundaries[j])
                if diff in hSideLengths:
                    maxSide = max(maxSide, diff)

        if maxSide == 0:
            return -1

        mod = 1000000007
        maxArea = (maxSide * maxSide) % mod

        return int(maxArea)