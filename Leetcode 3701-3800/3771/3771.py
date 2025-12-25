# Leetcode 3771: Total Score of Dungeon Runs
# https://leetcode.com/problems/total-score-of-dungeon-runs/
# Solved on 25th of December, 2025
import bisect


class Solution:
    def totalScore(self, hp: int, damage: list[int], requirement: list[int]) -> int:
        """
        Calculates the total score of dungeon runs.

        Args:
            hp (int): The initial health points of the player.
            damage (list[int]): A list of damage values for each dungeon.
            requirement (list[int]): A list of requirement values for each dungeon.

        Returns:
            int: The total score obtained from all dungeon runs.
        """
        n = len(damage)
        prefixSum = [0] * (n + 1)
        for i in range(n):
            prefixSum[i + 1] = prefixSum[i] + damage[i]

        totalPoints = 0
        for i in range(n):
            threshold = prefixSum[i + 1] + requirement[i] - hp
            idx = bisect.bisect_left(prefixSum, threshold, 0, i + 1)
            totalPoints += (i - idx + 1)

        return totalPoints