# Leetcode 3024: Type of Triangle
# https://leetcode.com/problems/type-of-triangle/
# Solved on 19th of May, 2025

class Solution:
    def triangleType(self, nums: list[int]) -> str:
        """
        Given an array of three integers, nums, representing the lengths of the sides of a triangle,
        determine the type of triangle based on the side lengths.

        Args:
            nums (list[int]): A list of three integers representing the side lengths of a triangle.

        Returns:
            str: A string representing the type of triangle: "equilateral", "isosceles", "scalene", or "none".
        """
        # Sort the lengths of the sides to easily apply the triangle inequality theorem
        # For N = 3, sorting takes constant time
        s1, s2, s3 = sorted(nums)

        # Check the triangle inequality theorem
        # If s1 + s2 <= s3, then the sides cannot form a valid triangle.
        # (The other two inequalities, s1 + s3 > s2 and s2 + s3 > s1, will always hold
        # if s1 + s2 > s3 because s3 is the longest side and side lengths are positive as per constraints).
        if (s1 + s2) <= s3:
            return "none"

        # If it's a valid triangle, classify its type.
        # This can be done by checking the number of unique side lengths
        unique_sides = len(set(nums))

        if unique_sides == 1:
            # All 3 sides are equal
            return "equilateral"
        elif unique_sides == 2:
            # 2 sides are equal
            return "isosceles"
        else:
            # All 3 sides are different
            return "scalene"