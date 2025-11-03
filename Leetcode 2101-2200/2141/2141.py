# Leetcode 2141: Maximum Running Time of N Computers
# https://leetcode.com/problems/maximum-running-time-of-n-computers/
# Solved on 3rd of November, 2025
class Solution:
    def maxRunTime(self, n: int, batteries: list[int]) -> int:
        """
        Calculates the maximum running time for 'n' computers given a list of batteries.

        Args:
            n (int): The number of computers.
            batteries (list[int]): A list of integers representing the capacity of each battery.

        Returns:
            int: The maximum running time all 'n' computers can operate simultaneously.
        """
        batteries.sort()

        m = len(batteries)

        extraPower = 0
        for i in range(m - n):
            extraPower += batteries[i]

        liveBatteries = batteries[(m - n):]
        currentLevel = liveBatteries[0]

        for i in range(1, n):
            diff = liveBatteries[i] - currentLevel
            powerNeeded = i * diff

            if extraPower >= powerNeeded:
                extraPower -= powerNeeded
                currentLevel = liveBatteries[i]
            else:
                currentLevel += extraPower // i
                return currentLevel

        currentLevel += extraPower // n
        return currentLevel