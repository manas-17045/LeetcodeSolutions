# Leetcode 2585: Number of Ways to Earn Points
# https://leetcode.com/problems/number-of-ways-to-earn-points/
# Solved on 13th of August, 2025
class Solution:
    def waysToReachTarget(self, target: int, types: list[list[int]]) -> int:
        """
        Calculates the number of ways to reach a target score given different types of questions.

        Args:
            target (int): The target score to reach.
            types (list[list[int]]): A list where each inner list [count, marks] represents a type of question,
                                     with 'count' being the number of questions of this type and 'marks' being the points for each question.

        Returns:
            int: The number of ways to reach the target score, modulo 10^9 + 7.
        """
        modulo = 10**9 + 7
        dp = [0] * (target + 1)
        dp[0] = 1

        for count, marks in types:
            for j in range(target, marks - 1, -1):
                for k in range(1, count + 1):
                    previousScore = j - k * marks
                    if previousScore >= 0:
                        dp[j] = (dp[j] + dp[previousScore]) % modulo
                    else:
                        break

        return dp[target]