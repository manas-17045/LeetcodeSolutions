# Leetcode 1473: Paint House III
# https://leetcode.com/problems/paint-house-iii/
# Solved on 6th of July, 2025
class Solution:
    def minCost(self, houses: list[int], cost: list[list[int]], m: int, n: int, target: int) -> int:
        """
        Calculates the minimum cost to paint a row of houses such that there are exactly `target` neighborhoods.

        A "neighborhood" is a group of consecutive houses painted with the same color.

        Args:
            houses: A list of integers where houses[i] is the color of the i-th house.
                    0 means the house needs to be painted.
            cost: A 2D list where cost[i][j] is the cost to paint house i with color j+1.
            m: The total number of houses.
            n: The total number of available colors.
            target: The desired number of neighborhoods.

        Returns:
            The minimum cost to paint the houses, or -1 if it's impossible.
        """
        INF = 10**18
        dp_prev = [[INF] * (n + 1) for _ in range(target + 1)]

        if houses[0] != 0:
            c = houses[0]
            dp_prev[1][c] = 0
        else:
            for c in range(1, (n + 1)):
                dp_prev[1][c] = cost[0][c - 1]

        # Iterate houses
        for i in range(1, m):
            dp_curr = [[INF] * (n + 1) for _ in range(target + 1)]
            for k in range(1, (target + 1)):
                for prev_c in range(1, (n + 1)):
                    prev_cost = dp_prev[k][prev_c]
                    if prev_cost == INF:
                        continue
                    # Determine possible current colors
                    if houses[i] != 0:
                        colors = [houses[i]]
                    else:
                        colors = range(1, (n + 1))
                    for c in colors:
                        # new neighborhood if color changes
                        nk = k + (1 if c != prev_c else 0)
                        if nk > target:
                            continue
                        paint_cost = 0 if houses[i] != 0 else cost[i][c - 1]
                        dp_curr[nk][c] = min(dp_curr[nk][c], prev_cost + paint_cost)
            dp_prev = dp_curr

        # Answer: exactly target neighborhoods
        ans = min(dp_prev[target][c] for c in range(1, (n + 1)))
        return -1 if ans >= INF else ans