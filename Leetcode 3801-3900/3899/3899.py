# Leetcode 3899: Angles of a Triangle
# https://leetcode.com/problems/angles-of-a-triangle/
# Solved on 27th of April, 2026
import math


class Solution:
    def internalAngles(self, sides: list[int]) -> list[float]:
        """
        Calculates the internal angles of a triangle given its side lengths.

        :param sides: A list of three integers representing the lengths of the sides.
        :return: A list of three floats representing the internal angles in degrees, sorted in ascending order. Returns an empty list if the sides do not form a valid triangle.
        """
        sortedSides = sorted(sides)
        if sortedSides[0] + sortedSides[1] <= sortedSides[2]:
            return []

        sideA = sortedSides[0]
        sideB = sortedSides[1]
        sideC = sortedSides[2]

        angleA = math.degrees(math.acos((sideB ** 2 + sideC ** 2 - sideA ** 2) / (2 * sideB * sideC)))
        angleB = math.degrees(math.acos((sideA ** 2 + sideC ** 2 - sideB ** 2) / (2 * sideA * sideC)))
        angleC = math.degrees(math.acos((sideA ** 2 + sideB ** 2 - sideC ** 2) / (2 * sideA * sideB)))

        return sorted([angleA, angleB, angleC])