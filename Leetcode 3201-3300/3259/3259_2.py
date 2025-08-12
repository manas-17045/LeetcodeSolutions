# Leetcode 3259: Maximum Energy Boost From Two Drinks
# https://leetcode.com/problems/maximum-energy-boost-from-two-drinks/
# Solved on 12th of August, 2025
class Solution:
    def maxEnergyBoost(self, energyDrinkA: list[int], energyDrinkB: list[int]) -> int:
        """
        Calculates the maximum energy boost achievable by strategically consuming energy drinks.

        Args:
            energyDrinkA (list[int]): A list of energy boosts provided by energy drink A at each stage.
            energyDrinkB (list[int]): A list of energy boosts provided by energy drink B at each stage.

        Returns:
            int: The maximum total energy boost.
        """
        n = len(energyDrinkA)
        if n == 0:
            return 0

        dp_a = energyDrinkA[0]
        dp_b = energyDrinkB[0]
        dp_s = 0

        for i in range(1, n):
            a = energyDrinkA[i]
            b = energyDrinkB[i]

            new_s = max(dp_a, dp_b, dp_s)
            new_a = max(dp_a, dp_s) + a
            new_b = max(dp_b, dp_s) + b

            dp_a = new_a
            dp_b = new_b
            dp_s = new_s

        return max(dp_a, dp_b, dp_s)