# Leetcode 3282: Reach End of Array With Max Score
# https://leetcode.com/problems/reach-end-of-array-with-max-score/
# Solved on 2nd of January, 2026
class Solution:
    def findMaximumScore(self, nums: list[int]) -> int:
        """
        Calculates the maximum score achievable by traversing the array.
        The score is calculated by summing the maximum element encountered so far up to each position (excluding the last).

        :param nums: A list of integers representing the array.
        :return: The maximum score achievable.
        """
        maxScore = 0
        currentMax = 0
        for i in range(len(nums) - 1):
            if nums[i] > currentMax:
                currentMax = nums[i]

            maxScore += currentMax

        return maxScore