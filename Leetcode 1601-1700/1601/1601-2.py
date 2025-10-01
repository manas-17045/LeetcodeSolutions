# Leetcode 1601: Maximum Number of Achievable Transfer Requests
# https://leetcode.com/problems/maximum-number-of-achievable-trannsfer-requests/
# Solved on 1st of October, 2025
class Solution:
    def maximumRequests(self, n: int, requests: list[list[int]]) -> int:
        """
        Calculates the maximum number of requests that can be fulfilled such that
        the net change in the number of people in each building is zero.

        Args:
            n (int): The number of buildings.
            requests (list[list[int]]): A list of requests, where each request `[from_building, to_building]`
                                        represents a person moving from `from_building` to `to_building`.
        Returns:
            int: The maximum number of requests that can be fulfilled.
        """
        maxCount = 0
        totalRequests = len(requests)

        for mask in range(1 << totalRequests):
            netChange = [0] * n
            count = 0

            for i in range(totalRequests):
                if mask & (1 << i):
                    fromBuilding = requests[i][0]
                    toBuilding = requests[i][1]
                    netChange[fromBuilding] -= 1
                    netChange[toBuilding] += 1
                    count += 1

            isValid = all(change == 0 for change in netChange)
            if isValid:
                maxCount = max(maxCount, count)

        return maxCount