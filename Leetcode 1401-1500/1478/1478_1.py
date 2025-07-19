# Leetcode 1478: Allocate Mailboxes
# https://leetcode.com/problems/allocate-mailboxes/
# Solved on 19th of July, 2025
class Solution:
    def minDistance(self, houses: list[int], k: int) -> int:
        """
        Calculates the minimum total distance between each house and its nearest mailbox.

        Args:
            houses: A list of integers representing the location of houses.
            k: The number of mailboxes to allocate.

        Returns:
            The minimum total distance.
        """
        numHouses = len(houses)
        houses.sort()

        cost = [[0] * numHouses for _ in range(numHouses)]
        for i in range((numHouses - 1), -1, -1):
            for j in range((i + 1), numHouses):
                cost[i][j] = cost[i + 1][j - 1] + houses[j] - houses[i]

        dp = [[float('inf')] * (k + 1) for _ in range(numHouses + 1)]

        dp[0][0] = 0

        # Fill the DP table
        for j in range(1, (k + 1)):
            for i in range(1, (numHouses + 1)):
                for p in range(i):
                    if dp[p][j - 1] != float('inf'):
                        lastGroupCost = cost[p][i - 1]
                        currentTotalCost = dp[p][j - 1] + lastGroupCost
                        dp[i][j] = min(dp[i][j], currentTotalCost)

        return int(dp[numHouses][k])