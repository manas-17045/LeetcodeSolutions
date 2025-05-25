# Leetcode 3362: Zero Array Transformation III
# https://leetcode.com/problems/zero-array-transformation-iii/
# Solved on 22nd May, 2025

import heapq

# Segment Tree for Point Query and Range Add Operations
class SegmentTree:
    def __init__(self, size: int):
        self.size = size
        self.tree = [0] * (4 * size)
        self.lazy = [0] * (4 * size)

    def _push_down(self, node_idx: int):
        if self.lazy[node_idx] != 0 and node_idx * 2 + 1 < len(self.tree):
            self.lazy[2 * node_idx] += self.lazy[node_idx]
            self.lazy[2 * node_idx + 1] += self.lazy[node_idx]

            # Update children's tree values directly
            self.tree[2 * node_idx] += self.lazy[node_idx]
            self.tree[2 * node_idx + 1] += self.lazy[node_idx]

            self.lazy[node_idx] = 0 # Reset lazy for current node

    def _range_add_recursive(self, node_idx: int, current_l: int, current_r: int, target_l: int, target_r: int, value: int):
        if current_l > target_r or current_r < target_l:    # No overlap
            return

        if target_l <= current_l and current_r <= target_r:  # Current segment fully within target range
            self.tree[node_idx] += value
            self.lazy[node_idx] += value
            return

        self._push_down(node_idx)  # Push lazy before splitting

        mid = (current_l + current_r) // 2
        self._range_add_recursive(2 * node_idx, current_l, mid, target_l, target_r, value)
        self._range_add_recursive(2 * node_idx + 1, mid + 1, current_r, target_l, target_r, value)

    def range_add(self, target_l: int, target_r: int, value: int):
        if target_l > target_r:  # Empty or invalid range
            return
        # Ensure calls are within bounds [0, self.size - 1]
        self._range_add_recursive(1, 0, self.size - 1, max(0, target_l), min(self.size - 1, target_r), value)

    def _query_point_recursive(self, node_idx: int, current_l: int, current_r: int, target_idx: int):
        if current_l == current_r:  # Leaf node
            return self.tree[node_idx]

        self._push_down(node_idx)

        mid = (current_l + current_r) // 2
        if target_idx <= mid:
            return self._query_point_recursive(2 * node_idx, current_l, mid, target_idx)
        else:
            return self._query_point_recursive(2 * node_idx + 1, mid + 1, current_r, target_idx)

    def query_point(self, target_idx: int) -> int:
        if not (0 <= target_idx < self.size):
            # This case should ideally not be hit if inputs are correct and target_idx is always valid.
            # For robustness, one might raise an error or return a defined value.
            return 0  # Or appropriate error handling
        return self._query_point_recursive(1, 0, self.size - 1, target_idx)

class Solution:
    def maxRemoval(self, nums: list[int], queries: list[list[int]]) -> int:
        """
        Calculates the maximum number of queries that can be removed such that
        the sum of coverages from the remaining queries at each index j is
        at least nums[j].

        This problem is equivalent to finding the minimum number of queries
        needed to satisfy the conditions and subtracting that from the total
        number of queries.

        Args:
            nums: A list of integers representing the minimum required coverage at each index.
            queries: A list of lists, where each inner list [l, r] represents a query covering indices from l to r.
        Returns:
            The maximum number of queries that can be removed, or -1 if it's impossible to satisfy the conditions.
        """
        n = len(nums)
        m = len(queries)

        if n == 0:  # No numbers to zero out, all queries can be removed
            return m

        # Initial Feasibility Check
        _diff_array = [0] * (n + 1)
        for l_q, r_q in queries:
            _diff_array[l_q] += 1
            if r_q + 1 <= n:    # Valid index for _diff_array of size (n + 1)
                _diff_array[r_q + 1] -= 1

        current_coverage_all_queries = 0
        for j_idx in range(n):
            current_coverage_all_queries += _diff_array[j_idx]
            if current_coverage_all_queries < nums[j_idx]:
                return -1   # Impossible even with all queries

        # Greedy selection of minimum queries
        queries_by_start = [[] for _ in range(n)]
        for q_details in queries:
            l, r = q_details
            queries_by_start[l].append((r, l))  # Store (r, l) pair for PQ

        st = SegmentTree(n) # Stores current coverage from chosen queries
        # active_queries_pq is a max-heap of (r, l) pairs, simulated with min-heap storing (-r, l)
        active_queries_pq = []

        chosen_queries_count = 0

        for j_idx in range(n):  # Sweep line over indices 0 to (n - 1)
            # Add queries starting at j_idx to the priority queue
            for r_val, l_val in queries_by_start[j_idx]:
                heapq.heappush(active_queries_pq, (-r_val, l_val))

            # Prune PQ: remove queries that have already ended (their r < current j_idx)
            while active_queries_pq and -active_queries_pq[0][0] < j_idx:
                heapq.heappop(active_queries_pq)

            coverage_at_j = st.query_point(j_idx)
            needed_additional_coverage = nums[j_idx] - coverage_at_j

            if needed_additional_coverage > 0:
                for _ in range(needed_additional_coverage):
                    # If PQ is empty or all its queries end before j_idx, demand cannot be met.
                    # This should not happen if the initial check passed.
                    if not active_queries_pq or -active_queries_pq[0][0] < j_idx:
                        # This indicates an inconsistency or that the problem is impossible
                        # under the greedy choices made, which means the initial check might
                        # not be sufficient or the greedy strategy doesn't apply perfectly.
                        # For standard interval covering to meet demands, this signifies impossibility.
                        return -1

                    neg_r_chosen, l_chosen = heapq.heappop(active_queries_pq)
                    r_chosen = -neg_r_chosen

                    chosen_queries_count += 1
                    st.range_add(l_chosen, r_chosen, 1) # Apply chosen query's coverage

        return m - chosen_queries_count