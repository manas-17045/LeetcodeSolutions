# Leetcode 3207: Maximum Points After Enemy Battles
# https://leetcode.com/problems/maximum-points-after-enemy-battles/
# Solved on 26th of November, 2025
class Solution:
    def maximumPoints(self, enemyEnergies: list[int], currentEnergy: int) -> int:
        """
        Calculates the maximum points obtainable after enemy battles.

        Args:
            enemyEnergies: A list of integers representing the energy of each enemy.
            currentEnergy: An integer representing the player's current energy.
        Returns:
            An integer representing the maximum points obtainable.
        """
        minVal = min(enemyEnergies)
        if currentEnergy < minVal:
            return 0
        totalEnergy = currentEnergy + sum(enemyEnergies) - minVal
        return totalEnergy // minVal