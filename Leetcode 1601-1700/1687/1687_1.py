# Leetcode 1687: Delivering Boxes from Storage to Ports
# https://leetcode.com/problems/delivering-boxes-from-storage-to-ports/
# Solved on 7th of August, 2025
import collections


class Solution:
    def boxDelivering(self, boxes: list[list[int]], portsCount: int, maxBoxes: int, maxWeight: int) -> int:
        """
        Calculates the minimum trips required to deliver all boxes.

        Args:
            boxes: A list of boxes, where each box is [port, weight, _].
            portsCount: The number of ports.
            maxBoxes: The maximum number of boxes that can be carried in one trip.
            maxWeight: The maximum weight that can be carried in one trip.

        Returns:
            The minimum number of trips required.
        """
        n = len(boxes)

        weightPrefix = [0] * (n + 1)
        changesPrefix = [0] * (n + 1)
        dp = [0] * (n + 1)

        diffs = [1 if i < (n - 1) and boxes[i][0] != boxes[i + 1][0] else 0 for i in range(n)]

        for i in range(n):
            weightPrefix[i + 1] = weightPrefix[i] + boxes[i][1]
            changesPrefix[i + 1] = changesPrefix[i] + diffs[i]

        q = collections.deque([0])

        for i in range(1, n + 1):
            while q and (q[0] < i - maxBoxes or weightPrefix[i] - weightPrefix[q[0]] > maxWeight):
                q.popleft()

            jBest = q[0]
            gMin = dp[jBest] + changesPrefix[jBest]
            dp[i] = 2 + changesPrefix[i - 1] + gMin

            g_i = dp[i] - changesPrefix[i]
            while q and (dp[q[-1]] - changesPrefix[q[-1]]) >= g_i:
                q.pop()
            q.append(i)

        return dp[n]