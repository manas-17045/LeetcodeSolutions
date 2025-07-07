# Leetcode 1223: Dice Roll Simulation
# https://leetcode.com/problems/dice-roll-simulation/
# Solved on 7th of July, 2025
class Solution:
    def dieSimulator(self, n: int, rollMax: list[int]) -> int:
        """
        Calculates the number of distinct sequences of rolls of a 6-sided die
        of length `n`, subject to the constraint that no face can be rolled
        more than `rollMax[face]` times consecutively.

        Args:
            n: The length of the sequence of rolls.
            rollMax: A list of 6 integers, where rollMax[i] is the maximum
                     number of consecutive times face `i` can be rolled.

        Returns:
            The number of distinct sequences modulo 10^9 + 7.
        """
        mod = 10**9 + 7

        dp = [[0] * 16 for _ in range(6)]

        for j in range(6):
            dp[j][1] = 1

        for i in range(2, (n + 1)):
            newDp = [[0] * 16 for _ in range(6)]

            sumPrevJ = [0] * 6
            totalPrev = 0
            for prevJ in range(6):
                currentSum = 0
                for prevK in range(1, (rollMax[prevJ] + 1)):
                    currentSum = (currentSum + dp[prevJ][prevK]) % mod
                sumPrevJ[prevJ] = currentSum
                totalPrev = (totalPrev + currentSum) % mod

            for j in range(6):
                newDp[j][1] = (totalPrev - sumPrevJ[j] + mod) % mod

                for k in range(2, (rollMax[j] + 1)):
                    newDp[j][k] = dp[j][k - 1]

            dp = newDp

        totalWays = 0
        for j in range(6):
            for k in range(1, (rollMax[j] + 1)):
                totalWays = (totalWays + dp[j][k]) % mod

        return totalWays