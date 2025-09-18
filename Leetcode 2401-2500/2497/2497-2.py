# Leetcode 2497: Maximum Star Sum of a Graph
# https://leetcode.com/problems/maximum-star-sum-of-a-graph/
# Solved on 18th of September, 2025
import heapq
from collections import defaultdict


class Solution:
    def maxStarSum(self, vals: list[int], edges: list[list[int]], k: int) -> int:
        """
        Calculates the maximum star sum in a graph. A star sum for a node is the sum of its value
        and the values of up to k of its neighbors, where only positive neighbor values are considered.
        :param vals: A list of integers representing the values of the nodes.
        :param edges: A list of lists representing the edges in the graph.
        :param k: An integer representing the maximum number of neighbors to include in a star sum.
        :return: The maximum star sum found in the graph.
        """
        n = len(vals)
        adj = defaultdict(list)
        for a, b in edges:
            adj[a].append(vals[b])
            adj[b].append(vals[a])

        # At minimum, the best star could be a single node (k = 0 case or no good neighbors).
        best = max(vals)

        for i in range(n):
            if k <= 0 or not adj.get(i):
                # No neighbors or not allowed to pick any edges.
                best = max(best, vals[i])
                continue

            # Pick up to k largest neighbor values
            top_k = heapq.nlargest(k, adj[i])
            # Only add positive contributions (negatives would reduce the star sum)
            cur_sum = vals[i]
            for v in top_k:
                if v > 0:
                    cur_sum += v
                else:
                    break

            best = max(best, cur_sum)

        return best