# Leetcode 2440: Create Components With Same Value
# https://leetcode.com/problems/create-components-with-same-value/
# Solved on 13th of June, 2025

class Solution:
    def componentValue(self, nums: list[int], edges: list[list[int]]) -> int:
        """
        Given an integer array nums of size n and a 2D integer array edges of size n - 1 where
        edges[i] = [ui, vi] represents a bidirectional edge between nodes ui and vi. The given
        edges form a tree.

        You are allowed to remove some edges, splitting the tree into multiple connected
        components. If you remove m edges, you will get m + 1 components.

        Return the maximum number of edges you can remove such that the sum of values of nums
        of all nodes in each component is equal.

        Args:
            nums: An integer array of node values.
            edges: A 2D integer array representing the tree edges.

        Returns:
            The maximum number of edges that can be removed.
        """
        n = len(nums)
        if n == 1:
            return 0

        # Build adjacency
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        # Compute parent[] and a post-order list of nodes
        parent = [-1] * n
        order = []
        stack = [0]
        parent[0] = 0   # Mark root's parent as itself
        while stack:
            u = stack.pop()
            order.append(u)
            for w in adj[u]:
                if w == parent[u]:
                    continue
                parent[w] = u
                stack.append(w)
        order.reverse() # Now 'oder' is a post-order

        total = sum(nums)
        mx = max(nums)

        # Enumerate all divisors of total, filter by >= mx, sort ascending
        divs = []
        i = 1
        while i * i <= total:
            if total % i == 0:
                if i >= mx:
                    divs.append(i)
                j = total // i
                if j != i and j >= mx:
                    divs.append(j)
            i += 1
        divs.sort()

        # For each candidate target sum, try to peel off subtrees of sum == target
        for target in divs:
            needed = total //target
            subSum = nums[:]
            count = 0
            ok = True
            for u in order:
                if subSum[u] == target:
                    count += 1
                else:
                    p = parent[u]
                    if p == u:
                        # Root did not match and cannot pass up => fail
                        ok = False
                        break
                    subSum[p] += subSum[u]

                # Early exit if too many
                if count > needed:
                    ok = False
                    break

            if ok and count == needed:
                return needed - 1

        return 0