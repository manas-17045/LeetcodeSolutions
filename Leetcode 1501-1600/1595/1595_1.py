# Leetcode 1595: Minimum Cost to Connect Two Groups of Points
# https://leetcode.com/problems/minimum-cost-to-connect-two-groups-of-points/
# Solved on 18th of July, 2025
import math


class Solution:
    def connectTwoGroups(self, cost: list[list[int]]) -> int:
        """
        Calculates the minimum cost to connect two groups of points.
        Args:
            cost: A 2D list where cost[i][j] is the cost to connect point i from group one to point j from group two.
        Returns:
            The minimum total cost to connect all points in both groups.
        """
        sizeOne = len(cost)
        sizeTwo = len(cost[0])

        costForPointToMask = [[0] * (1 << sizeTwo) for _ in range(sizeOne)]
        for i in range(sizeOne):
            for mask in range(1, 1 << sizeTwo):
                lsbIndex = (mask & -mask).bit_length() - 1
                prevMask = mask ^ (1 << lsbIndex)
                costForPointToMask[i][mask] = costForPointToMask[i][prevMask] + cost[i][lsbIndex]

        dp = [[math.inf] * (1 << sizeTwo) for _ in range(sizeOne)]

        for mask in range(1, 1 << sizeTwo):
            dp[0][mask] = costForPointToMask[0][mask]

        for i in range(1, sizeOne):
            for mask in range(1, 1 << sizeTwo):
                # Iterate over all non-empty submasks of mask for point i's connections
                submask = mask
                while submask > 0:
                    prevMask = mask ^ submask
                    # The cost is for previous points to cover prevMask, and for point i to cover submask.
                    currentCost = dp[i - 1][prevMask] + costForPointToMask[i][submask]
                    dp[i][mask] = min(dp[i][mask], currentCost)

                    # Also consider overlap, previous points cover `mask`. point i covers `submask`
                    overlapCost = dp[i - 1][mask] + costForPointToMask[i][submask]
                    dp[i][mask] = min(dp[i][mask], overlapCost)

                    submask = (submask - 1) & mask

        return int(dp[sizeOne - 1][(1 << sizeTwo) - 1])