# Leetcode 3373: Maximize the Number of Target Nodes After Connecting Trees II
# https://leetcode.com/problems/maximize-the-number-of-target-nodes-after-connecting-trees-ii/
# Solved on 29th of May, 2025
from collections import defaultdict, deque


class Solution:
    def maxTargetNodes(self, edges1: list[list[int]], edges2: list[list[int]]) -> list[int]:
        """
        Calculates the maximum number of target nodes reachable from each node in Tree 1.

        A target node is a pair (v, v') where v is a node in Tree 1 and v' is a node in Tree 2,
        such that the distance between the root of Tree 1 (node 0) and v in Tree 1, plus the
        distance between the root of Tree 2 (node 0) and v' in Tree 2, is even.

        The problem asks for the maximum number of such pairs (v, v') for each possible
        choice of a node i in Tree 1 and a node j in Tree 2, where the path is
        root_T1 -> ... -> i -> j -> ... -> v_prime. The total path length is
        d1(root_T1, i) + 1 + d2(j, v_prime). This needs to be even.
        This simplifies to d1(root_T1, i) and d2(j, v_prime) having different parities.

        Args:
            edges1: A list of edges representing Tree 1.
            edges2: A list of edges representing Tree 2.
        """
        n = 0
        # Determine n (number of nodes in Tree 1)
        # Constraints: n >= 2, so edges1 is non-empty. Node IDs are 0 to (n - 1).
        max_node1 = 0
        for u, v in edges1:
            max_node1 = max(max_node1, u, v)
        n = max_node1 + 1

        m = 0
        # Determine m (number of nodes in Tree 2)
        # Constraints: m >= 2, so edges2 is non-empty. Node IDs are 0 to (m - 1).
        max_node2 = 0
        for u, v in edges2:
            max_node2 = max(max_node2, u, v)
        m = max_node2 + 1

        # Get properties for Tree 1 and Tree 2
        parities1, num_c0_t1, num_c1_t1 = self.getTreeProperties(n, edges1, 0)
        parities2, num_c0_t2, num_c1_t2 = self.getTreeProperties(m, edges2, 0)

        # Calculate Tree 2's fixed contribution to target count
        # This is max(count of nodes with even distance from chosen 'j', count of nodes with odd distance from chosen 'j')
        # if we need d2(j,v') to be odd.
        # Path q -> j -> v_prime has length 1 + d2(j,v_prime). Needs to be even. So d2(j,v_prime) must be odd.
        # If j is C0_T2 (d2(root,j) is even), nodes v_prime with d2(j,v_prime) odd are C1_T2. Count is num_c1_t2.
        # If j is C1_T2 (d2(root,j) is odd), nodes v_prime with d2(j,v_prime) odd are C0_T2. Count is num_c0_t2.
        # Since m >= 2, Tree 2 has nodes of both parities from its root, so we can pick j to achieve max.
        t2_contrib = max(num_c0_t2, num_c1_t2)

        ans = [0] * n
        for i in range(n):
            # Contribution from Tree 1: depends on parity of node i from root_T1 (node 0)
            if parities1[i] == 0:   # Node i in Tree 1 has even distance from root_T1
                # targets in Tree 1 are nodes with same parity as i (i.e. C0_T1 nodes)
                ans[i] = num_c0_t1 + t2_contrib
            else:   # parities[i] == 1, node i in Tree 1 has odd distance from root_T1
                # Targets in Tree 1 are nodes with same parity as i (i.e. C1_T1 nodes)
                ans[i] = num_c1_t1 + t2_contrib

        return ans

    def getTreeProperties(self, num_nodes: int, edges: list[list[int]], root: int = 0):
        # Ensure num_nodes is at least 1 for root to be valid
        # Constraints n, , >= 2 imply num_nodes >= 2.
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        # parities[i] will store parity of distance from root: 0 for even, 1 for odd.
        parities = [-1] * num_nodes

        q = deque()

        if num_nodes > 0:   # root must be a valid index if num_nodes > 0
            parities[root] = 0
            q.append(root)
        else:   # Should not happen given constraints num_nodes >= 2
            return [], 0, 0

        while q:
            u = q.popleft()
            current_node_parity = parities[u]

            for v_neighbor in adj[u]:
                if parities[v_neighbor] == -1:  # Not visited
                    parities[v_neighbor] = 1 - current_node_parity  # (current_node_parity + 1) % 2
                    q.append(v_neighbor)

        num_color0 = 0  # Count of nodes with even distance from root
        num_color1 = 0  # Count of nodes with odd distance from root

        for i in range(num_nodes):
            if parities[i] == 0:
                num_color0 += 1
            elif parities[i] == 1:
                num_color1 += 1
            # else: parities[i] == -1. This means node i was not reached.
            # Given problem guarantees (valid tree, nodes 0..N-1), this should not occur.

        return parities, num_color0, num_color1