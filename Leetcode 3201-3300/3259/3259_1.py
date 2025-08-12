# Leetcode 3259: Maximum Energy Boost From Two Drinks
# https://leetcode.com/problems/maximum-energy-boost-from-two-drinks/
# Solved on 12th of August, 2025
class Solution:
    def maxEnergyBoost(self, energyDrinkA: list[int], energyDrinkB: list[int]) -> int:
        """
        Calculates the maximum energy boost achievable from two energy drinks.
        :param energyDrinkA: A list of integers representing the energy boost from drink A at each hour.
        :param energyDrinkB: A list of integers representing the energy boost from drink B at each hour.
        :return: The maximum total energy boost.
        """
        n = len(energyDrinkA)

        maxEnergyAPrev2 = energyDrinkA[0]
        maxEnergyBPrev2 = energyDrinkB[0]

        maxEnergyAPrev1 = energyDrinkA[1] + maxEnergyAPrev2
        maxEnergyBPrev1 = energyDrinkB[1] + maxEnergyBPrev2

        # Iterate from hour 2 to (n - 1)
        for i in range(2, n):
            maxEnergyACurrent = energyDrinkA[i] + max(maxEnergyAPrev1, maxEnergyAPrev2)
            maxEnergyBCurrent = energyDrinkB[i] + max(maxEnergyBPrev1, maxEnergyBPrev2)

            maxEnergyAPrev2 = maxEnergyAPrev1
            maxEnergyBPrev2 = maxEnergyBPrev1

            maxEnergyAPrev1 = maxEnergyACurrent
            maxEnergyBPrev1 = maxEnergyBCurrent

        return max(maxEnergyAPrev1, maxEnergyBPrev1)