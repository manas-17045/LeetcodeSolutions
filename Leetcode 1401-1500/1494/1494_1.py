# Leetcode 1494: Parallel Courses II
# https://leetcode.com/problems/parallel-courses-ii/
# Solved on 3rd of July, 2025
class Solution:
    def minNumberOfSemesters(self, n: int, relations: list[list[int]], k: int) -> int:
        """
        Calculates the minimum number of semesters required to complete all 'n' courses.

        Args:
            n (int): The total number of courses.
            relations (list[list[int]]): A list of prerequisite relations, where
                                         relations[i] = [prevCourse, nextCourse] means
                                         prevCourse must be taken before nextCourse.
            k (int): The maximum number of courses that can be taken in one semester.

        Returns:
            int: The minimum number of semesters needed to complete all courses.
        """
        preReqForCourse = [0] * n
        for prevCourse, nextCourse in relations:
            preReqForCourse[nextCourse - 1] |= 1 << (prevCourse - 1)

        dp = [n + 1] * (1 << n)
        dp[0] = n

        for mask in range(1 << n):
            if dp[mask] == n + 1:
                continue

            availableCourses = 0
            for i in range(n):
                if not (mask & (1 << i)):
                    if (preReqForCourse[i] & mask) == preReqForCourse[i]:
                        availableCourses |= (1 << i)

            subMask = availableCourses
            while subMask > 0:
                if bin(subMask).count('1') <= k:
                    nextMask = mask | subMask
                    if dp[nextMask] > dp[mask] + 1:
                        dp[nextMask] = dp[mask] + 1
                subMask = (subMask - 1) & availableCourses

        return dp[(1 << n) - 1]