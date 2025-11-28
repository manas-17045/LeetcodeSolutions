# Leetcode 2222: Number of Ways to Select Buildings
# https://leetcode.com/problems/number-of-ways-to-select-buildings/
# Solved on 28th of November, 2025
class Solution:
    def numberOfWays(self, s: str) -> int:
        """
        Calculates the number of ways to select three buildings such that they are of alternating types.

        Args:
            s (str): A binary string representing the types of buildings ('0' for one type, '1' for another).
        Returns:
            int: The total number of ways to select three buildings of alternating types.
        """
        zerosCount = s.count('0')
        onesCount = len(s) - zerosCount
        totalWays = 0
        zerosSoFar = 0
        onesSoFar = 0

        for char in s:
            if char == '0':
                totalWays += onesSoFar * (onesCount - onesSoFar)
                zerosSoFar += 1
            else:
                totalWays += zerosSoFar * (zerosCount - zerosSoFar)
                onesSoFar += 1

        return totalWays