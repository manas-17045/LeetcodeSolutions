# Leetcode 1691: Maximum Height by Stacking Cuboids
# https://leetcode.com/problems/maximum-height-by-stacking-cuboids/
# Solved on 20th of June, 2025

class Solution:
    def maxHeight(self, cuboids: list[list[int]]) -> int:
        """
        Calculates the maximum height of a stack of cuboids such that a cuboid
        can be placed on top of another if its dimensions are less than or equal
        to the dimensions of the cuboid below it (after rotating the cuboids).

        Args:
            cuboids: A list of lists, where each inner list represents the
                     dimensions [length, width, height] of a cuboid.

        Returns:
            The maximum possible height of a valid stack of cuboids.
        """

        # Normalize each cuboid
        for dims in cuboids:
            dims.sort()

        # Sort all cuboids lexicographically
        cuboids.sort()

        n = len(cuboids)
        # dp[i] = max stack height with cuboid i as the topmost block
        dp = [0] * n

        ans = 0
        for i in range(n):
            # At minimum, we can just take cuboid i by itself
            dp[i] = cuboids[i][2]
            # Try stacking on top of any j < i
            for j in range(i):
                if (cuboids[j][0] <= cuboids[i][0]) and (cuboids[j][1] <= cuboids[i][1]) and (cuboids[j][2] <= cuboids[i][2]):
                    dp[i] = max(dp[i], (dp[j] + cuboids[i][2]))

            ans = max(ans, dp[i])

        return ans