# Leetcode 3147: Taking Maximum Energy from the Mystic Dungeon
# https://leetcode.com/problems/taking-maximum-energy-from-the-mystic-dungeon/
# Solved on 10th of October, 2025
class Solution:
    def maximumEnergy(self, energy: list[int], k: int) -> int:
        """
        Calculates the maximum energy that can be taken from the mystic dungeon.
        :param energy: A list of integers representing the energy at each position.
        :param k: An integer representing the jump distance.
        :return: The maximum energy that can be collected.
        """
        n = len(energy)
        for i in range(n - k - 1, -1, -1):
            energy[i] += energy[i + k]
        return max(energy)