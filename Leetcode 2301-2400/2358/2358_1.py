# Leetcode 2358: Maximum Number of Groups Entering a Competition
# https://leetcode.com/problems/maximum-number-of-groups-entering-a-competition/
# Solved on 20th of June, 2025
import math


class Solution:
    def maximumGroups(self, grades: list[int]) -> int:
        """
        Given a list of grades, find the maximum number of groups that can be formed
        such that the sum of grades in each group is strictly greater than the sum
        of grades in the previous group, and the number of students in each group
        is strictly greater than the number of students in the previous group.

        The problem can be reduced to finding the largest integer k such that the sum
        of the first k integers (1 + 2 + ... + k) is less than or equal to the total
        number of students. This is because we can always sort the grades and form groups
        with increasing numbers of students (1, 2, 3, ... k) and increasing sums of grades.
        """
        numStudents = len(grades)

        discriminant = 1 + 8 * numStudents

        kFloat = (-1 + math.sqrt(discriminant)) / 2

        return int(kFloat)