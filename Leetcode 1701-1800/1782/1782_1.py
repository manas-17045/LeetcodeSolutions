# Leetcode 1782: Count Pairs of Nodes
# https://leetcode.com/problems/count-pairs-of-nodes/
# Solved on 23rd of June, 2025
from collections import Counter


class Solution:
    def countPairs(self, n: int, edges: list[list[int]], queries: list[int]) -> list[int]:
        """
        Counts the number of pairs of nodes (u, v) such that u < v and
        the sum of their degrees minus the number of shared edges between them
        is strictly greater than a given query value.

        Args:
            n: The number of nodes in the graph (1-indexed).
            edges: A list of lists, where each inner list [u, v] represents an edge
                   between node u and node v.
            queries: A list of integers, where each integer is a query value.

        Returns:
            A list of integers, where each element is the count of valid pairs
            for the corresponding query value.
        """
        nodeDegrees = [0] * (n + 1)
        sharedEdgeCounts = Counter()

        for u, v in edges:
            nodeDegrees[u] += 1
            nodeDegrees[v] += 1

            if u > v:
                u, v = v, u
            sharedEdgeCounts[(u, v)] += 1

        # sortedDegrees contains degree values for nodes 1 to n, sorted.
        sortedDegrees = sorted(nodeDegrees[i] for i in range(1, (n + 1)))

        queryResults = []
        for currentQueryValue in queries:
            currentPairCount = 0
            left, right = 0, (n - 1)

            # Two-pointer approach to count pairs (a, b)
            while left < right:
                if sortedDegrees[left] + sortedDegrees[right] > currentQueryValue:
                    currentPairCount += (right - left)
                    right -= 1
                else:
                    left += 1

            # Adjust count for pairs that have shared edges.
            for (node1, node2), numSharedEdges in sharedEdgeCounts.items():
                degreeSum = nodeDegrees[node1] + nodeDegrees[node2]

                # Check if this pair was counted by the initial two-pointer sum.
                wasCountedByDegreeSum = (degreeSum > currentQueryValue)

                actualIncidentValue = degreeSum - numSharedEdges
                # Check if this pair should be counted based on its true incident value.
                shouldActuallyBeCounted = (actualIncidentValue > currentQueryValue)

                if wasCountedByDegreeSum and not shouldActuallyBeCounted:
                    currentPairCount -= 1
                elif not wasCountedByDegreeSum and shouldActuallyBeCounted:
                    currentPairCount += 1

            queryResults.append(currentPairCount)

        return queryResults