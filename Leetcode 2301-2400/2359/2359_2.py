# Solved on 30th of May, 2025

class Solution:
    def closestMeetingNode(self, edges: list[int], node1: int, node2: int) -> int:
        """
        Finds the node that is reachable from both node1 and node2 and minimizes the maximum distance from either node.

        Args:
            edges: A list representing the directed edges of a graph. edges[i] is the node that node i points to, or -1 if there is no outgoing edge.
            node1: The starting node for the first traversal.
            node2: The starting node for the second traversal.

        Returns:
            The index of the node that minimizes the maximum distance from node1 and node2.
            If multiple nodes satisfy this condition, the node with the smallest index is returned.
            If no such node exists, -1 is returned.

        """
        n = len(edges)

        # Helper function to compute distance from `start` to every node (or inf if unreachable)
        def computeDistances(start: int) -> list[int]:
            dist = [float('inf')] * n
            curr = start
            d = 0
            # Walk along the unique outgoing edges until we hit -1 or a visited node
            while curr != -1 and dist[curr] == float('inf'):
                dist[curr] = d
                d += 1
                curr = edges[curr]
            return dist

        # Compute distances from both nodes
        d1 = computeDistances(node1)
        d2 = computeDistances(node2)

        # Find the node i minimizing max(d1[i], d2[i]), tie-breaking on smaller i
        answer = -1
        best = float('inf')
        for i in range(n):
            m = max(d1[i], d2[i])
            if m < best:
                best = m
                answer = i

        return answer