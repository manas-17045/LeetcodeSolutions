# Leetcode 2860: Happy Students
# https://leetcode.com/problems/happy-students/
# Solved on 28th of June, 2025
class Solution:
    def countWays(self, nums: list[int]) -> int:
        """
        Calculates the number of ways to select a group of students such that
        all selected students are happy and all unselected students are sad.

        A student is happy if selected and their `nums[i]` value is less than
        the total number of selected students. A student is sad if unselected
        and their `nums[i]` value is greater than or equal to the total number of selected students.
        """
        numStudents = len(nums)
        nums.sort()
        happyWays = 0

        if nums[0] > 0:
            happyWays += 1

        for groupSize in range(1, numStudents):
            if nums[groupSize - 1] < groupSize < nums[groupSize]:
                happyWays += 1

        happyWays += 1

        return happyWays