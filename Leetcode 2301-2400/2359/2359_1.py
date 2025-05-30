# Leetcode 2359: Find Closest Node to Given Two Nodes
# https://leetcode.com/problems/find-closest-node-to-given-two-nodes/
# Solved on 30th of May, 2025

class Solution:
    def closestMeetingNode(self, edges: list[int], node1: int, node2: int) -> int:
        """
        Finds the node that is closest to both node1 and node2.

        The distance between two nodes is the number of edges on the path between them.
        A node is considered "closest" if the maximum of its distances from node1 and node2
        is minimized. If there are multiple such nodes, the one with the smallest index is returned.

        Args:
            edges: A list representing the directed graph where edges[i] is the node that node i points to.
                   A value of -1 indicates no outgoing edge.
            node1: The starting node for the first path.
            node2: The starting node for the second path.

        Returns:
            The index of the node that minimizes the maximum distance from node1 and node2.
            Returns -1 if no such node exists (i.e., node1 and node2 are not in the same component
            that allows them to reach a common node).
        """
        n = len(edges)

        # Helper function to compute distances from a start_node
        def getDistances(start_node: int, graph_edges: list[int], num_nodes: int) -> list[int]:
            node_distances = [-1] * num_nodes

            current_distance = 0
            current_node = start_node

            # Traverse the path starting from start_node.
            while current_node != -1 and node_distances[current_node] == -1:
                node_distances[current_node] = current_distance
                current_node = graph_edges[current_node]
                current_distance += 1

            return node_distances

        # Compute distances from node1 to all other nodes and node2 to all other nodes.
        distancesFromNode1 = getDistances(node1, edges, n)
        distancesFromNode2 = getDistances(node2, edges, n)

        minFoundMaxDist = float('inf')
        meetingNodeCandidate = -1

        # Iterate through all nodes to find the one that minimizes the maximum distance from node1 and node2.
        for i in range(n):
            if distancesFromNode1[i] != -1 and distancesFromNode2[i] != -1:
                maxDistToNodeI = max(distancesFromNode1[i], distancesFromNode2[i])
                if maxDistToNodeI < minFoundMaxDist:
                    minFoundMaxDist = maxDistToNodeI
                    meetingNodeCandidate = i

        return meetingNodeCandidate