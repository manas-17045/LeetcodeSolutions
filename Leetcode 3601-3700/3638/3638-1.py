# Leetcode 3638: Maximum Balanced Shipments
# https://leetcode.com/problems/maximum-balanced-shipments/
# Solved on 3rd of September, 2025
class Solution:
    def maxBalancedShipments(self, weight: list[int]) -> int:
        """
        Calculates the maximum number of balanced shipments.

        Args:
            weight (list[int]): A list of integers representing the weights of parcels.
        Returns:
            int: The maximum number of balanced shipments.
        """
        numParcels = len(weight)

        prevGreater = [-1] * numParcels
        stack = []
        for i in range(numParcels):
            while stack and weight[stack[-1]] <= weight[i]:
                stack.pop()
            if stack:
                prevGreater[i] = stack[-1]
            stack.append(i)

        dp = [0] * (numParcels + 1)
        prefixMaxDp = [0] * (numParcels + 1)

        for i in range(1, numParcels + 1):
            dp[i] = dp[i - 1]

            parcelIndex = i - 1
            anchorIndex = prevGreater[parcelIndex]

            if anchorIndex != -1:
                newCount = 1 + prefixMaxDp[anchorIndex]
                dp[i] = max(dp[i], newCount)

            prefixMaxDp[i] = max(prefixMaxDp[i - 1], dp[i])

        return dp[numParcels]