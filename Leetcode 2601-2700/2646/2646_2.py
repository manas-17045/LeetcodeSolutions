# Leetcode 2646: Minimize the Total Price of the Trips
# https://leetcode.com/problems/minimize-the-total-price-of-the-trips/
# Solved on 14th of June, 2025
from collections import deque


class Solution:
    def minimumTotalPrice(self, n: int, edges: list[list[int]], price: list[int], trips: list[list[int]]) -> int:
        """
        Calculates the minimum total price to complete all trips by optionally halving the price of certain nodes.

        The problem can be modeled as a tree where nodes represent locations and edges represent connections.
        Each node has an initial price. We are given a list of trips, where each trip is a path between two nodes.
        We can choose to halve the price of any node, but if a node's price is halved, its adjacent nodes' prices
        cannot be halved. The goal is to minimize the total cost of all trips, where the cost of a trip is the sum
        of the prices of the nodes on its path, considering any halving.

        Args:
            n: The number of nodes in the tree.
            edges: A list of edges representing the connections between nodes.
            price: A list of integers where price[i] is the initial price of node i.
            trips: A list of trips, where each trip is a list [start_node, end_node].

        Returns:
            The minimum total price to complete all trips.
        """
        # Build tree adjacency
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        # Count how many times each node appears across all trip-paths
        freq = [0] * n

        def markPath(s: int, t: int):
            # BFS from s to t to record parents
            parent = {s: -1}
            q = deque([s])
            while q:
                u = q.popleft()
                if u == t:
                    break
                for w in adj[u]:
                    if w not in parent:
                        parent[w] = u
                        q.append(w)

            # Reconstruct path from t back to s
            cur = t
            while cur != -1:
                freq[cur] += 1
                cur = parent[cur]

        for s, t in trips:
            markPath(s, t)

        saving = [freq[i] * (price[i] // 2) for i in range(n)]

        def dfs(u: int, p: int) -> (int, int):
            dp0 = 0
            dp1 = saving[u]
            for w in adj[u]:
                if w == p:
                    continue
                c0, c1 = dfs(w, u)
                dp0 += max(c0, c1)  # If we don't halve u, child may or may not be halved
                dp1 += c0   # If we do halve u, child cannot be halved
            return dp0, dp1

        dp0_root, dp1_root = dfs(0, -1)
        bestSaving = max(dp0_root, dp1_root)

        # Total un-discounted cost
        totalCost = sum(freq[i] * price[i] for i in range(n))
        return totalCost - bestSaving