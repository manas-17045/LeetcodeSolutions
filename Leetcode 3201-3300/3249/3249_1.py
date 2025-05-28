# Leetcode 3249: Count The Number of Good Nodes
# https://leetcode.com/problems/count-the-number-of-good-nodes/
# Solved on 28th of May, 2025
from collections import deque


class Solution:
    def countGoodNodes(self, edges: list[list[int]]) -> int:
        """
        Counts the number of "good" nodes in a tree rooted at node 0.

        A node is considered "good" if all the subtrees rooted at its children have the same size.
        Leaf nodes are considered good by definition (vacuously true).

        Args:
            edges: A list of lists representing the edges of the tree. Each inner list [u, v]
                   indicates an edge between nodes u and v. The tree is rooted at node 0.

        Returns:
            The total count of good nodes in the tree.
        """
        n = len(edges) + 1

        # Constraints state n >= 2.
        # If n = 1 were possible (no edges, single node tree):
        # if n == 1: # Root node 0, is a leaf.
        #    return 1 # Leaf nodes are good by vacuous truth.

        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        children_map = [[] for _ in range(n)]

        # BFS from root 0 to:
        # 1. Build children_map (representing the directed tree structure rooted at 0).
        # 2. Get traversal_order (nodes in BFS order; parents appear before their children).
        #    This order, when reversed, is suitable for post-order traversal calculations like subtree sizes.
        traversal_order = []

        q = deque()
        # The problem specifies the tree is rooted at node 0.
        q.append(0)
        # visited_bfs tracks nodes already added to the queue to avoid cycles and redundant processing,
        # and correctly establishes parent-child relationships in the BFS tree.
        visited_bfs = {0}

        while q:
            u = q.popleft()
            traversal_order.append(u)

            for v_neighbor in adj[u]:
                # If v_neighbor has not been visited, it's a child of u in this BFS-derived tree.
                if v_neighbor not in visited_bfs:
                    visited_bfs.add(v_neighbor)
                    children_map[u].append(v_neighbor)
                    q.append(v_neighbor)

        # Calculate subtree_sizes for all nodes.
        # The size of a node's subtree is 1 (for the node itself) plus the sum of the subtree sizes of its children.
        # Initialize subtree_sizes: each node's subtree contains at least itself.
        subtree_sizes = [1] * n

        # Iterate in reverse of traversal_order (effectively a post-order traversal).
        # This ensures that when processing a node u, the subtree sizes of all its children
        # (which appear later in traversal_order and thus earlier in this reversed loop)
        # have already been computed and finalized.
        # Iterate from the last element of traversal_order to the first
        for i in range(n - 1, -1, -1):
            u_node = traversal_order[i]
            for child_node in children_map[u_node]:
                subtree_sizes[u_node] += subtree_sizes[child_node]

        # Count good nodes based on the problem's definition:
        # "A node is good if all the subtrees rooted at its children have the same size."
        good_nodes_count = 0
        # Iterate through each node from 0 to (n - 1).
        for i in range(n):
            current_node_children = children_map[i]

            if not current_node_children:
                # If a node is a leaf (has no children), the condition "all its children..."
                # is vacuously true. So, leaf nodes are good.
                good_nodes_count += 1
                continue

            # If the node has children, compare their subtree sizes.
            # Get the subtree size of the first child to use as a reference.
            first_child_subtree_size = subtree_sizes[current_node_children[0]]
            # Assume good until proven otherwise.
            is_current_node_good = True

            # Check if all other children have the same subtree size as the first child.
            for child_idx in range(1, len(current_node_children)):
                child_node = current_node_children[child_idx]
                if subtree_sizes[child_node] != first_child_subtree_size:
                    is_current_node_good = False
                    break   # Mismatch found, node is not good.

            if is_current_node_good:
                good_nodes_count += 1

        return good_nodes_count