# Leetcode 1406: Stone Game III
# https://leetcode.com/problems/stone-game-iii/
# Solved on 27th of July, 2025
class Solution:
    def stoneGameIII(self, stoneValue: list[int]) -> str:
        """
        Determines the winner of the Stone Game III.

        Alice and Bob take turns removing 1, 2, or 3 stones from the beginning of the row.
        The player who collects the most points wins.
        :param stoneValue: A list of integers representing the value of each stone.
        :return: "Alice" if Alice wins, "Bob" if Bob wins, or "Tie" if it's a tie.
        """

        n = len(stoneValue)
        dp = [0] * 4

        for i in range(n - 1, -1, -1):
            currentStonesSum = 0
            maxDiff = float('-inf')
            for k in range(1, 4):
                if i + k <= n:
                    currentStonesSum += stoneValue[i + k - 1]
                    diff = currentStonesSum - dp[(i + k) % 4]
                    maxDiff = max(maxDiff, diff)
            dp[i % 4] = maxDiff

        finalScore = dp[0]

        if finalScore > 0:
            return "Alice"
        elif finalScore < 0:
            return "Bob"
        else:
            return "Tie"