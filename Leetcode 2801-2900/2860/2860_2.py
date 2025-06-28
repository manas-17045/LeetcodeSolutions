# Leetcode 2860: Happy Students
# https://leetcode.com/problems/happy-students/
# Solved on 28th of June, 2025
import bisect


class Solution:
    def countWays(self, nums: list[int]) -> int:
        """
        Counts the number of ways to select a non-empty subset of students such
        that for each selected student, their skill level is less than the
        total number of selected students, and for each unselected student,
        their skill level is greater than or equal to the total number of
        selected students.

        Args:
            nums: A list of integers representing the skill levels of students.

        Returns:
            The number of ways to select students satisfying the conditions.

        The problem can be rephrased as finding the number of possible values
        for `k` (the number of selected students) such that exactly `k` students
        have skill levels less than `k`, and no students have skill levels equal to `k`.
        """
        n = len(nums)
        nums.sort()
        ans = 0

        # Try every possible selected-size k from 0 to n
        for k in range(n + 1):
            # number of elements < k
            lt = bisect.bisect_left(nums, k)
            # number of elements == k
            eq = bisect.bisect_right(nums, k) - lt

            # valid if exactly k elements are < k (so they must be selected)
            # and none are == k (since those students would be unhappy)
            if lt == k and eq == 0:
                ans += 1

        return ans