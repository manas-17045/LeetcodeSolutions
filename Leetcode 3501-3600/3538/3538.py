# Leetcode 3538: Merge Operations for Minimum Travel Time
# https://leetcode.com/problems/merge-operations-for-minimum-travel-time/
# Solved on 16th of December, 2025
class Solution:
    def minTravelTime(self, l: int, n: int,k: int, position: list[int], time: list[int]) -> int:
        """
        Calculates the minimum travel time for a series of merge operations.

        Args:
            l (int): The length of the road (not directly used in the provided solution).
            n (int): The total number of initial items.
            k (int): The number of items to be removed.
            position (list[int]): A list of integers representing the positions of the items.
            time (list[int]): A list of integers representing the time associated with each item.
        Returns:
            int: The minimum total travel time.
        """
        m = n - k

        p_sum = [0] * (n + 1)
        for i in range(n):
            p_sum[i + 1] = p_sum[i] + time[i]

        dp = [[float('inf')] * n for _ in range(n)]

        for i in range(1, n):
            dp[i][0] = (position[i] - position[0]) * time[0]

        for cnt in range(3, m + 1):
            new_dp = [[float('inf')] * n for _ in range(n)]

            for curr in range(cnt - 1, n):
                for prev in range(cnt - 2, curr):
                    dist = position[curr] - position[prev]

                    min_prev_cost = float('inf')

                    for pp in range(cnt - 3, prev):
                        if dp[prev][pp] == float('inf'):
                            continue

                        rate = p_sum[prev + 1] - p_sum[pp + 1]

                        cost = dp[prev][pp] + dist * rate
                        if cost < min_prev_cost:
                            min_prev_cost = cost

                    new_dp[curr][prev] = min_prev_cost

            dp = new_dp

        ans = float('inf')
        for prev in range(m - 2, n - 1):
            if dp[n - 1][prev] < ans:
                ans = dp[n - 1][prev]

        return int(ans)