# Leetcode 2029: Stone Game IX
# https://leetcode.com/problems/stone-game-ix/
# Solved on 5th of March, 2026
class Solution:
    def stoneGameIX(self, stones: list[int]) -> bool:
        """
        Determines if Alice can win the stone game given the rules of divisibility by 3.

        :param stones: A list of integers representing the values of the stones.
        :return: True if Alice wins, False otherwise.
        """
        remainderCounts = [0, 0, 0]
        for stoneValue in stones:
            remainderCounts[stoneValue % 3] += 1

        if remainderCounts[0] % 2 == 0:
            return remainderCounts[1] > 0 and remainderCounts[2] > 0

        return abs(remainderCounts[1] - remainderCounts[2]) > 2