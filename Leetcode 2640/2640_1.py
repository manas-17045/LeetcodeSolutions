# Leetcode 2640: Find the Score of All Prefixes of an Array
# https://leetcode.com/problems/find-the-score-of-all-prefixes-of-an-array/

class Solution:
    def findPrefixScore(self, nums: list[int]) -> list[int]:
        """
        Calculate the prefix score for a list of integers. The prefix score is determined
        by adding up the conversion values at each index. The conversion value for an
        index is calculated as the sum of the current number and the maximum number
        encountered so far in the list.

        The function iterates through the list, maintaining a running maximum `current_max`
        and a cumulative score `current_score`. At each index, it calculates the
        conversion value by adding the current number to the `current_max` and updates
        the `current_score` with the current conversion value. The results are stored
        in a list and returned.

        :param nums: List of integers for which the prefix score is to be calculated
        :type nums: list[int]
        :return: A list of integers representing the prefix scores at every index
        :rtype: list[int]
        """
        n = len(nums)
        ans = []

        current_max = 0
        current_score = 0

        for i in range(n):
            current_max = max(current_max, nums[i])
            conversion_i = nums[i] + current_max

            current_score += conversion_i
            ans.append(current_score)

        return ans