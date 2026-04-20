# Leetcode 2078: Two Furthest Houses With Different Colors
# https://leetcode.com/problems/two-furthest-houses-with-different-colors/
# Solved on 20th of April, 2026
class Solution:
    def maxDistance(self, colors: list[int]) -> int:
        """
        Finds the maximum distance between two houses with different colors.

        :param colors: A list of integers representing the color of each house.
        :return: The maximum distance between two houses with different colors.
        """
        arrayLength = len(colors)
        rightIndex = arrayLength - 1

        while colors[rightIndex] == colors[0]:
            rightIndex -= 1

        leftIndex = 0
        while colors[leftIndex] == colors[-1]:
            leftIndex += 1

        return max(rightIndex, arrayLength - 1 - leftIndex)