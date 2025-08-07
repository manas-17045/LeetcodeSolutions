# Leetcode 1687: Delivering Boxes from Storage to Ports
# https://leetcode.com/problems/delivering-boxes-from-storage-to-ports/
# Solved on 7th of August, 2025
from collections import deque


class Solution:
    def boxDelivering(self, boxes: list[list[int]], portsCount: int, maxBoxes: int, maxWeight: int) -> int:
        """
        Calculates the minimum number of trips to deliver all boxes.

        Args:
            boxes: A list of lists, where each inner list represents a box and contains two integers:
                   the destination port and the weight of the box.
            portsCount: The total number of ports.
            maxBoxes: The maximum number of boxes that can be carried in a single trip.
            maxWeight: The maximum total weight of boxes that can be carried in a single trip.

        Returns:
            The minimum number of trips required to deliver all the boxes.
        """
        n = len(boxes)
        ports = [b[0] for b in boxes]
        weights = [b[1] for b in boxes]

        # prefix[i] = number of times port changes between boxes[0..i]
        prefix = [0] * n
        for i in range(1, n):
            prefix[i] = prefix[i-1] + (1 if ports[i] != ports[i-1] else 0)

        # dp[i] = min trips to deliver first i boxes
        dp = [0] + [10**18] * n

        dq = deque([0])  # will store candidate start-indices j for dp
        j = 0            # left of our current sliding window
        weight_sum = 0

        for i in range(1, n+1):
            # Add box i-1 into current window
            weight_sum += weights[i-1]

            # Shrink window until within capacity
            while i - j > maxBoxes or weight_sum > maxWeight:
                weight_sum -= weights[j]
                j += 1

            # Drop any deque entries that are no longer in [j..i-1]
            while dq and dq[0] < j:
                dq.popleft()

            # The best start for delivering up to i is dq[0]
            best_start = dq[0]
            # trips = dp[best_start] + (port changes in [best_start..i-1]) + 2 (go + return)
            dp[i] = dp[best_start] + (prefix[i-1] - (prefix[best_start] if best_start > 0 else 0)) + 2

            # Prepare i as a future candidate (except after the last box)
            if i < n:
                # Maintain deque in increasing order of (dp[x] - prefix[x])
                cur_val = dp[i] - prefix[i]
                while dq and (dp[dq[-1]] - prefix[dq[-1]]) >= cur_val:
                    dq.pop()
                dq.append(i)

        return dp[n]