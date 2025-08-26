# Leetcode 2742: Painting the Walls
# https://leetcode.com/problems/painting-the-walls/
# Solved on 26th of August, 2025
from functools import lru_cache


class Solution:
    def paintWalls(self, cost: list[int], time: list[int]) -> int:
        """
        Calculates the minimum cost to paint all walls.

        Args:
            cost (list[int]): A list where cost[i] is the cost to paint the i-th wall.
            time (list[int]): A list where time[i] is the time taken to paint the i-th wall.
        Returns:
            int: The minimum cost to paint all walls.
        """

        n = len(cost)
        # Precompute each item's contribution (cap at n to keep states small)
        weights = [min(time[i] + 1, n) for i in range(n)]
        INF = 10**18

        @lru_cache(maxsize=None)
        def dp(idx: int, rem: int) -> int:
            if rem <= 0:
                return 0
            if idx == n:
                return INF

            # Skip current wall
            best = dp(idx + 1, rem)
            # Take current wall
            take = cost[idx] + dp(idx + 1, rem - weights[idx])
            if take < best:
                best = take
            return best

        ans = dp(0, n)
        return ans if ans < INF else -1