# Leetcode 1691: Maximum Height by Stacking Cuboids
# https://leetcode.com/problems/maximum-height-by-stacking-cuboids/
# Solved on 20th of June, 2025
import itertools


class Solution:
    def maxHeight(self, cuboids: list[list[int]]) -> int:
        """
        Calculates the maximum possible height of a stack of cuboids,
        where a cuboid can be placed on top of another if its dimensions
        (width, length, and height) are all less than or equal to the
        corresponding dimensions of the cuboid below it. Cuboids can be
        rotated.

        Args:
            cuboids: A list of lists, where each inner list represents a
                     cuboid with dimensions [width, length, height].

        Returns:
            The maximum possible height of a stack of cuboids.
        """
        numOriginalCuboids = len(cuboids)

        # Generate candidate bricks from all permutations of dimensions for each cuboid.
        candidateBricks = []
        for i in range(numOriginalCuboids):
            dims = cuboids[i]
            for p in itertools.permutations(dims):
                candidateBricks.append((p[0], p[1], p[2], i))

        # Sort candidate bricks
        candidateBricks.sort(reverse=True)

        numCandidateBricks = len(candidateBricks)

        if numCandidateBricks == 0:
            return 0

        # ---DP Programming---
        # dp[i] stores the maximum height of a stack whose TOP brick is candidateBricks[i].
        dp = [0] * numCandidateBricks
        maxTotalHeight = 0

        for i in range(numCandidateBricks):
            currentBrickW, currentBrickL, currentBrickH, currentBrickId = candidateBricks[i]

            # Initialize dp[i] with the height of the current brick itself (stack of one).
            dp[i] = currentBrickH

            # Check all previously processed bricks (j < i) to see if currentBrick can be place on them.
            for j in range(i):
                prevBrickW, prevBrickL, prevBrickH, prevBrickId = candidateBricks[j]

                if (currentBrickW <= prevBrickW) and (currentBrickL <= prevBrickL) and (currentBrickH <= prevBrickH):
                    # Also, they must be from different original cuboids.
                    if currentBrickId != prevBrickId:
                        dp[i] = max(dp[i], (dp[j] + currentBrickH))

            # Update the overall maximum height found so far
            maxTotalHeight = max(maxTotalHeight, dp[i])

        return maxTotalHeight