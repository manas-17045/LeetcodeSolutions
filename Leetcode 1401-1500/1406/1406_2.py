# Leetcode 1406: Stone Game III
# https://leetcode.com/problems/stone-game-iii/
# Solved on 27th of July, 2025
class Solution:
    def stoneGameIII(self, stoneValue: list[int]) -> str:
        """
        Determines the winner of a stone game where players take 1, 2, or 3 stones.

        Args:
            stoneValue (list[int]): A list of integers representing the value of each stone.
        Returns:
            str: "Alice" if Alice wins, "Bob" if Bob wins, or "Tie" if the game is a tie.
        """
        n = len(stoneValue)
        # dp1 = dp[i+1], dp2 = dp[i+2], dp3 = dp[i+3]; beyond end they are 0
        dp1 = dp2 = dp3 = 0

        # Iterate from the end backwards
        for i in range(n - 1, -1, -1):
            best = float('-inf')
            total = 0
            # Try taking k stones
            # After taking k stones, opponent's best diff is dp[i+k], so our net is total - dp[i+k]
            for k, dp_next in ((1, dp1), (2, dp2), (3, dp3)):
                if i + k - 1 < n:
                    total += stoneValue[i + k - 1]
                    best = max(best, total - dp_next)
            # Roll the window
            dp3, dp2, dp1 = dp2, dp1, best

        # dp1 now holds dp[0]: the best score difference Alice can achieve over Bob
        if dp1 > 0:
            return "Alice"
        elif dp1 < 0:
            return "Bob"
        else:
            return "Tie"