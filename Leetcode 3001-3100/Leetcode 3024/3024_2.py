# Leetcode 3024: Type of Triangle
# https://leetcode.com/problems/type-of-triangle/
# Solved on 19th of May, 2025

class Solution:
    def triangleType(self, nums: list[int]) -> str:
        """
        Determines the type of triangle based on the lengths of its sides.

        Args:
            nums: A list of three integers representing the lengths of the sides.

        Returns:
            A string representing the type of triangle: "equilateral", "isosceles", "scalene", or "none" if the sides do not form a valid triangle.
        """
        # Sort the lengths of the sides for easy inequality checks
        a, b, c = sorted(nums)
        # Triangle inequality: sum of two shorted > longest
        if a + b <= c:
            return "none"

        # All sides are equal
        if a == c:
            return "equilateral"
        # Exactly two sides are equal
        if a == b or b == c:
            return "isosceles"
        # All sides are different
        return "scalene"