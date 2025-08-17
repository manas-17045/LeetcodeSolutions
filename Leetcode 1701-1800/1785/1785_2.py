# Leetcode 1785: Minimum Elements to Add to Form a Given Sum
# https://leetcode.com/problems/minimum-elements-to-add-to-form-a-given-sum/
# Solved on 17th of August, 2025
class Solution:
    def minElements(self, nums: list[int], limit: int, goal: int) -> int:
        """
        Calculates the minimum number of elements needed to add to `nums` such that the sum of `nums` equals `goal`.
        Each added element must have an absolute value less than or equal to `limit`.
        :param nums: A list of integers.
        :param limit: An integer representing the maximum absolute value of an element that can be added.
        :param goal: An integer representing the target sum.
        :return: The minimum number of elements required to reach the goal.
        """
        total = sum(nums)
        diff = goal - total

        if diff == 0:
            return 0

        # Minimum number of moved to size `limit` to cover abs(diff)
        return (abs(diff) + limit - 1) // limit