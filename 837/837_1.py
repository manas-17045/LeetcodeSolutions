# Leetcode 837: New 21 Game
# https://leetcode.com/problems/new-21-game/
# Solved on 17th of August, 2025
class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        """
        Calculates the probability of winning the New 21 Game.

        Args:
            n (int): The maximum score allowed. If a player's score exceeds n, they lose.
            k (int): The target score. If a player's score reaches or exceeds k, they stop drawing cards.
            maxPts (int): The maximum number of points a card can have. Cards are drawn uniformly from 1 to maxPts.

        Returns:
            float: The probability that Alice wins the game.
        """
        if k == 0 or n >= k + maxPts:
            return 1.0

        dp = [0.0] * (n + 1)
        dp[0] = 1.0
        windowSum = 1.0
        probability = 0.0

        for i in range(1, n + 1):
            dp[i] = windowSum / maxPts

            if i < k:
                windowSum += dp[i]
            else:
                probability += dp[i]

            if i >= maxPts:
                windowSum -= dp[i - maxPts]

        return probability