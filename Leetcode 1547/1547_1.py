# Leetcode 1547: Minimum Cost to Cut a Stick
# https://leetcode.com/problems/minimum-cost-to-cut-a-stick/
# Solved on 16th of May, 2025
from functools import lru_cache


class Solution:
    def minCost(self, n: int, cuts: list[int]) -> int:
        """
        Calculates the minimum cost to cut a stick of length 'n' at the positions specified in 'cuts'.

        The cost of each cut is the length of the stick being cut.  The goal is to find the minimum total cost
        to make all the cuts.  This is solved using dynamic programming with memoization (top-down approach).

        Args:
            n: The length of the stick.
            cuts: A list of integers representing the positions where the stick should be cut.

        Returns:
            The minimum total cost to make all the cuts.
        """

        # Augment cuts with the stick's endpoints and sort.
        # These define all boundaries of segments we might consider.
        cuts_extended = sorted([0] + cuts + [n])
        num_boundaries = len(cuts_extended)

        # Use memoization (top-down DP) to store results of subproblem.
        # dp_solve(left_boundary_idx, right_boundary_idx) returns the minimum cost
        # to make all cuts within the segment (cuts_extended[left_boundary_idx], cuts_extended_idx[right_boundary_idx]).
        @lru_cache(None)
        def dp_solve(left_boundary_idx: int, right_boundary_idx: int) -> int:
            # Base case: If the segment is too small to contain any cuts
            # (i.e., no k such that left_boundary_idx < k < right_boundary_idx),
            # the cost is 0. This occurs when right_boundary_idx is adjacent to or before left_boundary_idx.
            if right_boundary_idx <= left_boundary_idx + 1:
                return 0

            min_total_cost_for_segment = float('inf')

            # The cost of performing the *first* cut on the current segment
            # is the length of this segment.
            current_segment_length = cuts_extended[right_boundary_idx] - cuts_extended[left_boundary_idx]

            # Try every possible cut point 'k' within the current segment as the *first* cut.
            # k_idx is an index into cuts_extended.
            for k_idx in range(left_boundary_idx + 1, right_boundary_idx):
                # The cut is made at cuts_extended[k_idx].
                # Cost = (cost of this first cut) + (min cost for left sub-segment) + (min cost for right sub-segment)
                cost_if_k_is_first_cut = (current_segment_length + dp_solve(left_boundary_idx, k_idx) + dp_solve(k_idx, right_boundary_idx))
                min_total_cost_for_segment = min(min_total_cost_for_segment, cost_if_k_is_first_cut)

            return min_total_cost_for_segment

        # The main problem is to find the min cost for the entire stick,
        # which runs from cuts_extended[0] (which is 0) to cuts_extended[num_boundaries - 1] (which is n).
        result = dp_solve(0, num_boundaries - 1)

        # For environments where the Solution object might be reused for multiple test cases,
        # clearing the cache can be good practice, though not always strictly needed by platforms.
        dp_solve.cache_clear()

        return result