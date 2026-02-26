# Leetcode 2139: Minimum Moves to Reach Target Score
# https://leetcode.com/problems/minimum-moves-to-reach-target-score/
# Solved on 26th of February, 2026
class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        """
        Calculates the minimum number of moves to reach the target score starting from 1.
        You can either increment by 1 or double the current value (if maxDoubles > 0).

        :param target: The integer target score to reach.
        :param maxDoubles: The maximum number of times the doubling operation can be used.
        :return: The minimum number of moves as an integer.
        """
        totalMoves = 0

        while target > 1 and maxDoubles > 0:
            totalMoves += 1 + (target % 2)
            target //= 2
            maxDoubles -= 1

        return totalMoves + target - 1