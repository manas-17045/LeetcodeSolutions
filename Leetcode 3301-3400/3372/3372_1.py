# Leetcode 3372: Maximize the Number of Target Nodes After Connecting Trees I
# https://leetcode.com/problems/maximize-the-number-of-target-nodes-after-connecting-trees-i/
# Solved on 28th of May, 2025
import collections


class Solution:
    def maxTargetNodes(self, edges1: list[list[int]], edges2: list[list[int]], k: int) -> list[int]:
        """
        Calculates the maximum number of target nodes reachable after connecting two trees.

        Args:
            edges1: A list of edges representing the first tree.
            edges2: A list of edges representing the second tree.
            k: The maximum allowed distance from the connection point.

        Returns:
            A list where the i-th element is the maximum number of target nodes
            reachable when connecting node i of the first tree to some node
            in the second tree, such that the distance from the connection point
            to any target node is at most k.
        """
        n1: int
        if not edges1:
            # Tree with 1 node (node 0) if edges list is empty
            n1 = 1
        else:
            # Assuming node labels are within [0, N - 1] and it's a valid tree
            # N = len(edges) + 1
            n1 = len(edges1) + 1

        n2: int
        if not edges2:
            n2 = 1
        else:
            n2 = len(edges2) + 1

        # Adjacency list for Tree 1
        adj1: list[list[int]] = [[] for _ in range(n1)]
        for u, v in edges1:
            adj1[u].append(v)
            adj1[v].append(u)

        # Adjacency list for Tree 2
        adj2: list[list[int]] = [[] for _ in range(n2)]
        for u, v in edges2:
            adj2[u].append(v)
            adj2[v].append(u)

        # Helper function to perform BFS and count nodes within max_d
        def bfs_count_nodes_in_dist(start_node: int, max_d: int, current_adj_list: list[list[int]], num_nodes_in_tree: int) -> int:
            # No nodes can be reached if max distance is negative
            if max_d < 0:
                return 0

            q = collections.deque()
            # visited array is generally faster than a set for dense 0...N-1 integer IDs
            visited = [False] * num_nodes_in_tree

            # Add start_node to queue, mark visited. Distance to self is 0.
            # If 0 <= max_d, count self. This is handled by max_d < 0 check above.
            q.append((start_node, 0))
            visited[start_node] = True
            # Counting start_node itself
            count = 1

            while q:
                curr, d = q.popleft()

                # If current node's distance equals max_d, we can't explore its neighbors further
                if d == max_d:
                    continue

                # Explore neighbors
                for neighbor in current_adj_list[curr]:
                    if not visited[neighbor]:   # If neighbor not visited
                        visited[neighbor] = True    # Mark visited
                        count += 1  # Increment count
                        q.append((neighbor, d + 1)) # Add neighbor to queue with distance (d + 1)
            return count

        # Calculate Count_1(i, k) for all i in Tree 1
        # N1_values[i] stores the number of nodes in Tree 1 within distance k from node i.
        N1_values = [0] * n1
        for i in range(n1): # For each node i in Tree 1
            N1_values[i] = bfs_count_nodes_in_dist(i, k, adj1, n1)

        # Calculate MaxCount_2(k - 1)
        # This is max_{j in V2} Count_2(j, k - 1)
        # M2_val stores this maximum.
        M2_val = 0
        if k - 1 >= 0:  # Only proceed if k - 1 is a non-negative distance
            max_nodes_found_in_tree2 = 0
            for j in range(n2): # Try connecting to each node j in Tree 2
                count_N2_j = bfs_count_nodes_in_dist(j, k - 1, adj2, n2)
                if count_N2_j > max_nodes_found_in_tree2:
                    max_nodes_found_in_tree2 = count_N2_j
            M2_val = max_nodes_found_in_tree2

        # If (k - 1) < 0 (i.e., k = 0), M2_val remains 0, which is correct as no nodes in Tree 2 can be reached.

        # Construct the final answer array
        # For each node i in Tree 1, answer[i] = Count_1(i, k) + MaxCount_2(k - 1)
        answer = [0] * n1
        for i in range(n1):
            answer[i] = N1_values[i] + M2_val

        return answer