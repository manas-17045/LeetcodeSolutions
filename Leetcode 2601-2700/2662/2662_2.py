# Leetcode 2662: Minimum Cost of a Path With Special Roads
# https://leetcode.com/problems/minimum-cost-of-a-path-with-special-roads/
# Solved on 24th of August, 2025
import heapq


class Solution:
    def minimumCost(self, start: list[int], target: list[int], specialRoads: list[list[int]]) -> int:
        """
        Calculates the minimum cost to travel from a start point to a target point,
        considering both Manhattan distance and special roads with specific costs.

        :param start: A list of two integers [sx, sy] representing the starting coordinates.
        :param target: A list of two integers [tx, ty] representing the target coordinates.
        :param specialRoads: A list of lists, where each inner list [x1, y1, x2, y2, cost] represents a special road from (x1, y1) to (x2, y2) with a given cost.
        :return: An integer representing the minimum cost to reach the target.
        """
        sx, sy = start
        tx, ty = target

        # Collect points: include target and all special road endpoints
        pts = [(tx, ty)]
        for x1, y1, x2, y2, c in specialRoads:
            pts.append((x1, y1))
            pts.append((x2, y2))

        # Deduplicate points and build index mapping
        idx = {}
        uniq = []
        for p in pts:
            if p not in idx:
                idx[p] = len(uniq)
                uniq.append(p)

        n = len(uniq)
        target_idx = idx[(tx, ty)]

        # Map special-road start index -> list of (end_index, cost)
        special_map = {}
        for x1, y1, x2, y2, c in specialRoads:
            a = idx[(x1, y1)]
            b = idx[(x2, y2)]
            special_map.setdefault(a, []).append((b, c))

        def manhattan(a, b):
            return abs(a[0] - b[0]) + abs(a[1] - b[1])

        # Initialize distances: cost to reach each node directly from start (Manhattan)
        INF = 10 ** 18
        dist = [INF] * n
        for i, p in enumerate(uniq):
            dist[i] = manhattan((sx, sy), p)

        # Dijkstra using a min-heap
        heap = [(dist[i], i) for i in range(n)]
        heapq.heapify(heap)

        while heap:
            d, u = heapq.heappop(heap)
            if d != dist[u]:
                continue
            # If we've reached the target node, it's the minimum possible cost
            if u == target_idx:
                return d

            ux, uy = uniq[u]

            # Relax special roads that start from this node
            if u in special_map:
                for v, cost in special_map[u]:
                    nd = d + cost
                    if nd < dist[v]:
                        dist[v] = nd
                        heapq.heappush(heap, (nd, v))

            # Relax Manhattan moves to every other node (implicit complete graph)
            for v in range(n):
                if v == u:
                    continue
                vx, vy = uniq[v]
                nd = d + abs(ux - vx) + abs(uy - vy)
                if nd < dist[v]:
                    dist[v] = nd
                    heapq.heappush(heap, (nd, v))

        # If heap exhausted, return distance to target index
        return dist[target_idx]