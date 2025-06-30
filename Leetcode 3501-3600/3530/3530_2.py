# Leetcode 3530: Maximum Profit from Valid Topological Order in DAG
# https://leetcode.com/problems/maximum-profit-from-valid-topological-order-in-dag/
# Solved on 29th of June, 2025
class Solution:
    def maxProfit(self, n: int, edges: list[list[int]], score: list[int]) -> int:
        """
        Calculates the maximum profit achievable by ordering nodes, considering prerequisites and scores.

        The problem asks to find an ordering of all `n` nodes such that the total profit is maximized.
        The profit for a node `i` placed at position `p` (1-indexed) is `score[i] * p`.
        There are `edges` representing prerequisites: if `(u, v)` is an edge, `u` must come before `v`.

        This problem can be modeled as finding a topological sort that maximizes a weighted sum.
        Since `n` is small (up to 15), dynamic programming with bitmask can be used.

        Args:
            n: The total number of nodes.
            edges: A list of prerequisite edges, where `edges[i] = [u, v]` means `u` must come before `v`.
            score: A list of scores for each node, where `score[i]` is the score of node `i`.

        Returns:
            The maximum profit achievable.
        """
        # prereq[i] will be a bitmask of all nodes that must come before i
        prereq = [0] * n
        for u, v in edges:
            prereq[v] |= 1 << u

        full = (1 << n) - 1
        # dp[mask] = max profit for ordering exactly the nodes in 'mask' in positions 1...popcount(mask)
        dp = [-1] * (1 << n)
        dp[0] = 0

        for mask in range(1 << n):
            if dp[mask] < 0:
                # This subset isn't reachable by any valid order.
                continue

            # Next position index (1-based) is popcount(mask) + 1
            next_pos = mask.bit_count() + 1

            # Try to add any node i that's not yet in mask and whose prerequisites are satisfied
            free = full ^ mask
            m = free
            while m:
                i = (m & -m).bit_length() - 1
                m &= m - 1

                # If all prereqs of 1 are already in mask
                if (mask & prereq[i]) == prereq[i]:
                    new_mask = mask | (1 << i)
                    profit = dp[mask] + score[i] * next_pos
                    if profit > dp[new_mask]:
                        dp[new_mask] = profit

        return dp[full]