# Leetcode 837: New 21 Game
# https://leetcode.com/problems/new-21-game/
# Solved on 17th of August, 2025
class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        """
        Calculates the probability of winning the New 21 Game.
        :param n: The maximum score to reach or exceed to win.
        :param k: The maximum score to draw a new card.
        :param maxPts: The maximum points a card can have.
        :return: The probability of winning the game.
        """
        if k == 0:
            return 1.0

        if n >= k + maxPts - 1:
            return 1.0

        dp = [0.0] * (n + 1)
        dp[0] = 1.0
        window_sum = 1.0
        res = 0.0

        for i in range(1, (n + 1)):
            dp[i] = window_sum / maxPts

            if i >= k:
                res += dp[i]
            else:
                window_sum += dp[i]

            if i - maxPts >= 0:
                window_sum -= dp[i - maxPts]

        return res