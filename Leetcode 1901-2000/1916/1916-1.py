# Leetcode 1916: Count Ways to Build Rooms in an Ant Colony
# https://leeetcode.com/problems/count-ways-to-build-rooms-in-an-ant-colony/
# Solved on 27th of September, 2025
import sys
sys.setrecursionlimit(10**5 + 5)

class Solution:
    def waysToBuildRooms(self, prevRoom: list[int]) -> int:
        """
        Calculates the number of ways to build rooms in an ant colony.

        :param prevRoom: A list where prevRoom[i] is the parent of room i, or -1 if room i is the root.
        :return: The total number of ways to build the rooms, modulo 1,000,000,007.
        """
        n = len(prevRoom)
        mod = 1_000_000_007

        adj = [[] for _ in range(n)]
        for i, p in enumerate(prevRoom):
            if p != -1:
                adj[p].append(i)

        fact = [1] * (n + 1)
        invFact = [1] * (n + 1)
        for i in range(1, n + 1):
            fact[i] = (fact[i - 1] * i) % mod

        invFact[n] = pow(fact[n], mod - 2, mod)
        for i in range(n - 1, -1, -1):
            invFact[i] = (invFact[i + 1] * (i + 1)) % mod

        def getCombinations(n_val, k_val):
            if k_val < 0 or k_val > n_val:
                return 0
            numerator = fact[n_val]
            denominator = (invFact[k_val] * invFact[n_val - k_val]) % mod
            return (numerator * denominator) % mod

        def dfs(u):
            roomSoFar = 0
            ways = 1
            for v in adj[u]:
                childSize, childWays = dfs(v)

                ways = (ways * childWays) % mod

                combinations = getCombinations(roomSoFar + childSize, childSize)
                ways = (ways * combinations) % mod

                roomSoFar += childSize

            return (roomSoFar + 1, ways)

        _, totalWays = dfs(0)
        return totalWays