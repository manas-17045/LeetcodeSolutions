# Leetcode 1601: Maximum Number of Achievable Transfer Requests
# https://leetcode.com/problems/maximum-number-of-achievable-trannsfer-requests/
# Solved on 1st of October, 2025
class Solution:
    def maximumRequests(self, n: int, requests: list[list[int]]) -> int:
        """
        Calculates the maximum number of achievable transfer requests.

        Args:
            n (int): The number of buildings.
            requests (list[list[int]]): A list of transfer requests, where each request is [from_building, to_building].

        Returns:
            int: The maximum number of achievable transfer requests.
        """
        numRequests = len(requests)
        maxCount = 0

        for i in range(1 << numRequests):
            balance = [0] * n
            currentCount = 0

            for j in range(numRequests):
                if (i >> j) & 1:
                    currentCount += 1
                    sourceBuilding = requests[j][0]
                    destBuilding = requests[j][1]
                    balance[sourceBuilding] -= 1
                    balance[destBuilding] += 1

            isBalanced = True
            for buildingBalance in balance:
                if buildingBalance != 0:
                    isBalanced = False
                    break

            if isBalanced:
                maxCount = max(maxCount, currentCount)

        return maxCount