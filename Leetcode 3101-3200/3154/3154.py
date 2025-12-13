# Leetcode 3154: Find Number of Ways to Reach the K-th Stair
# https://leetcode.com/problems/find-number-of-ways-to-reach-the-k-th-stair/
# Solved on 13th of December, 2025
class Solution:
    def waysToReachStair(self, k: int) -> int:
        """
        Calculates the number of ways to reach the k-th stair.

        :param k: The target stair number.
        :return: The number of ways to reach the k-th stair.
        """
        memo = {}

        def solve(currentStair, jump, canGoDown):
            state = (currentStair, jump, canGoDown)
            if state in memo:
                return memo[state]

            count = 0
            if currentStair == k:
                count += 1

            if currentStair > k + 1:
                return 0

            if canGoDown and currentStair > 0:
                count += solve(currentStair - 1, jump, False)

            count += solve(currentStair + (1 << jump), jump + 1, True)

            memo[state] = count
            return count

        return solve(1, 0, True)