# Leetcode 1857: Largest Color Value in a Directed Graph
# https://leetcode.com/problems/largest-color-value-in-a-directed-graph/
# Solved on 26th of May, 2025
from collections import deque


class Solution:
    def largestPathValue(self, colors: str, edges: list[list[int]]) -> int:
        """
        Calculates the largest color value of any path in a directed graph.

        The color value of a path is defined as the number of nodes on the path
        that have the most frequent color on that path.

        Args:
            colors: A string where colors[i] is the color of the i-th node.
                    Colors are lowercase English letters.
            edges: A list of lists representing the directed edges of the graph.
                   edges[i] = [u, v] means there is a directed edge from node u to node v.

        Returns:
            The largest color value among all paths in the graph.
            Returns -1 if the graph contains a cycle.
        """

        n = len(colors)
        # Constraint: 1 <= n <= 10^5, so n is at least 1

        adj = [[] for _ in range(n)]
        in_degree = [0] * n

        for u_node, v_node in edges:
            # Constraints: 0 <= u_node, v_node < n, so direct indexing is safe
            adj[u_node].append(v_node)
            in_degree[v_node] += 1

        # dp[node_idx][color_idx] stores the maximum count of the color
        # (represented by color_idx, 0-25 for 'a'-'z') on any path ending at node_idx.
        dp = [[0] * 26 for _ in range(n)]

        queue = deque()
        for i in range(n):
            if in_degree[i] == 0:
                queue.append(i)
                # Initialize DP for source nodes:
                # A path consisting of only the source node i has a count of 1 for its own color.
                dp[i][ord(colors[i]) - ord('a')] = 1

        max_path_color_value = 0  # Stores the result to be returned
        processed_node_count = 0

        while queue:
            u = queue.popleft()
            processed_node_count += 1

            # Update the overall maximum color value.
            # max(dp[u]) is the color value of the best path ending at u.
            # (Color value of a path = count of its most frequent color)
            # This takes the maximum of the 26 color counts for paths ending at u.
            current_max_for_node_u = 0
            for color_count in dp[u]:
                current_max_for_node_u = max(current_max_for_node_u, color_count)
            max_path_color_value = max(max_path_color_value, current_max_for_node_u)

            for v in adj[u]:  # For each neighbor v of u
                color_v_as_int = ord(colors[v]) - ord('a')
                for c_idx in range(26):  # For each possible color 'a' through 'z'

                    # Count of color c_idx on a path ending at u
                    count_from_u = dp[u][c_idx]

                    # If this color c_idx is the same as color of node v, increment count by 1
                    # when extending the path to v.
                    new_count_for_v_path = count_from_u + (1 if c_idx == color_v_as_int else 0)

                    # Update dp[v][c_idx] if path through u provides a higher count for c_idx
                    # for paths ending at v.
                    dp[v][c_idx] = max(dp[v][c_idx], new_count_for_v_path)

                in_degree[v] -= 1
                if in_degree[v] == 0:  # If all predecessors of v are processed
                    queue.append(v)

        if processed_node_count != n:
            # Not all nodes were processed, indicating a cycle in the graph.
            return -1
        else:
            # All nodes processed, graph is a DAG.
            # If n >= 1 and it's a DAG, max_path_color_value >= 1.
            # This is because source nodes are processed, and for a source u,
            # current_max_for_node_u will be at least dp[u][color_of_u] = 1.
            return max_path_color_value