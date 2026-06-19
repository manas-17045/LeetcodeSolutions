# Leetcode 1732: Find the Highest Altitude
# https://leetcode.com/problems/find-the-highest-altitude/
# Solved on 19th of June, 2026
class Solution:
    def largestAltitude(self, gain: list[int]) -> int:
        """
        Finds the highest altitude of a point.

        :param gain: Net altitude gains between consecutive points.
        :type gain: list[int]
        :return: The highest altitude.
        :rtype: int
        """
        maxAltitude = 0
        currentAltitude = 0
        for netGain in gain:
            currentAltitude += netGain
            if currentAltitude > maxAltitude:
                maxAltitude = currentAltitude

        return maxAltitude