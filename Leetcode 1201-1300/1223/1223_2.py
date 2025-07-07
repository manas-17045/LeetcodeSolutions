# Leetcode 1223: Dice Roll Simulation
# https://leetcode.com/problems/dice-roll-simulation/
# Solved on 7th of July, 2025
class Solution:
    def dieSimulator(self, n: int, rollMax: list[int]) -> int:
        """
        Calculates the number of distinct sequences of dice rolls of length 'n'
        such that no face appears more than 'rollMax[face]' times consecutively.

        This problem can be solved using dynamic programming.

        Let dp[j][k] be the number of sequences of length 'i' (current iteration)
        ending with face 'j' appearing exactly 'k' times consecutively.

        Args:
            n (int): The length of the dice roll sequence.
            rollMax (list[int]): A list where rollMax[i] is the maximum number
                                 of consecutive times the face 'i' can appear.

        Returns:
            int: The total number of distinct sequences modulo 10^9 + 7.
        """
        mod = 10**9 + 7
        prev = [[0] * 16 for _ in range(6)]
        for face in range(6):
            prev[face][1] = 1
        for _ in range(2, (n + 1)):
            curr = [[0] * 16 for _ in range(6)]
            total = sum(sum(prev[f][1:rollMax[f] + 1]) for f in range(6)) % mod
            for face in range(6):
                blocked = sum(prev[face][1:rollMax[face] + 1]) % mod
                curr[face][1] = (total - blocked) % mod
                for cnt in range(2, rollMax[face] + 1):
                    curr[face][cnt] = prev[face][cnt - 1]
            prev = curr
        return sum(sum(prev[f][1:rollMax[f] + 1]) for f in range(6)) % mod