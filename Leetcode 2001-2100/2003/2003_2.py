# Leetcode 2003: Smallest Missing Genetic Value in Each Subtree
# https://leetcode.com/problems/smallest-missing-genetic-value-in-each-subtree/
# Solved on 25th of June, 2025
import sys
sys.setrecursionlimit(10 ** 7)


class Solution:
    def smallestMissingValueSubtree(self, parents: list[int], nums: list[int]) -> list[int]:
        """
        Calculates the smallest missing positive integer value for each subtree in a given tree.

        The problem asks us to find, for each node `i`, the smallest positive integer that is not present
        in the subtree rooted at `i`.

        Args:
            parents: A list of integers where `parents[i]` is the parent of node `i`.
                     `parents[i] == -1` for the root node.
            nums: A list of integers where `nums[i]` is the value of node `i`.

        Returns:
            A list of integers `ans` where `ans[i]` is the smallest missing positive integer
            in the subtree rooted at node `i`.

        The solution uses a clever approach by starting from the node containing the value 1 and
        iteratively moving up to the root, processing subtrees along the way.
        """
        n = len(parents)
        # Build adjacency list of children
        children = [[] for _ in range(n)]
        root = -1
        for i, p in enumerate(parents):
            if p == -1:
                root = i
            else:
                children[p].append(i)

        # If 1 is not in nums, every subtree is missing 1
        if 1 not in nums:
            return [1] * n

        # Prepare
        maxV = max(nums)
        size = max(maxV, n) + 2
        seen = [False] * size
        ans = [1] * n

        # Helper function: Iterative DFS to mark all values in subtree rooted at u
        def markSubtree(u: int) -> None:
            stack = [u]
            while stack:
                node = stack.pop()
                val = nums[node]
                if not seen[val]:
                    seen[val] = True
                    for c in children[node]:
                        stack.append(c)

        # Find the node having value 1
        idx1 = nums.index(1)

        missing = 1
        prev = -1
        node = idx1

        # Climb from the '1' node up to the root
        while node != -1:
            # Mark the ancestor itself (if not the first pass)
            if prev != -1:
                v = nums[node]
                if not seen[v]:
                    seen[v] = True
                # Mark all other branches (children except the path we came from)
                for c in children[node]:
                    if c != prev:
                        markSubtree(c)
            else:
                markSubtree(node)

            # Advance missing until a value not yet seen
            while seen[missing]:
                missing += 1
            ans[node] = missing

            # Move up
            prev = node
            node = parents[node]

        return ans
