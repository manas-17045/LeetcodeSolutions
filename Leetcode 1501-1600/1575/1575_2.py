# Leetcode 1575: Count All Possible Routes
# https://leetcode.com/problems/count-all-possible-routes/
# Solved on 13th of July, 2025
import sys
sys.setrecursionlimit(10**7)


class Solution:
    def countRoutes(self, locations: list[int], start: int, finish: int, fuel: int) -> int:
        """
        Counts the number of possible routes from a start city to a finish city
        given a list of city locations and an initial amount of fuel.

        A route is valid if it starts at 'start', ends at 'finish', and the
        fuel never drops below zero. You can visit cities multiple times.

        Args:
            locations: A list of integers representing the positions of cities.
            start: The index of the starting city.
            finish: The index of the finishing city.
            fuel: The initial amount of fuel.
        Returns:
            The number of valid routes modulo 10^9 + 7.
        """
        MOD = 10**9 + 7
        n = len(locations)

        dp = [[-1] * (fuel + 1) for _ in range(n)]

        def dfs(cur: int, f: int) -> int:
            if dp[cur][f] != -1:
                return dp[cur][f]

            # If we're sitting at the finish, that's one valid route (we can stop here)
            res = 1 if cur == finish else 0

            # Try moving to every other city
            for nxt in range(n):
                if nxt == cur:
                    continue
                cost = abs(locations[cur] - locations[nxt])
                if f >= cost:
                    res = (res + dfs(nxt, f - cost)) % MOD

            dp[cur][f] = res
            return res

        return dfs(start, fuel)