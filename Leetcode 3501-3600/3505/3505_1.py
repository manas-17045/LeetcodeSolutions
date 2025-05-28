# Leetcode 3505: Minimum Operations to Make Elements Within K Subarrays Equal
# https://leetcode.com/problems/minimum-operations-to-make-elements-within-k-subarrays-equal/
# Solved on 27th of May, 2025
import heapq
from collections import defaultdict, deque


class Solution:
    def minOperations(self, nums: list[int], x: int, k: int) -> int:
        """
        Calculates the minimum number of operations to make elements within k non-overlapping
        subarrays of length x equal. An operation consists of changing an element's value.
        The cost of making a subarray equal is the sum of absolute differences between each
        element and the median of that subarray.

        Args:
            nums: A list of integers.
            x: The length of each subarray.
            k: The number of non-overlapping subarrays.

        Returns:
            The minimum total operations required. Returns 0 if no operations are needed
            or if it's impossible to select k such subarrays.
        """
        n = len(nums)

        # costs[i] = min operations to make nums[i...i + x - 1] equal
        costs = [float('inf')] * (n - x + 1)

        # Constraints: 2 <= x <= nums.length, k*x <= nums.length.
        # So, n-x+1 is well-defined and >= 1.
        # If x=0 (not allowed by constraints), or k=0 (not allowed), result could be 0.

        small_h = []    # max-heap for smaller-half, stores (-value, original_index)
        large_h = []    # min-heap for larger-half, stores (value, original_index)

        value_locations = {}    # Maps (value, original_index) -> 0 (small_h) or 1 (large_h)

        s_sum_active, s_cnt_active = 0, 0
        l_sum_active, l_cnt_active = 0, 0

        removed_markers = defaultdict(int)  # Maps heap_item_representation to count

        def _clean_heap_top(h): # No need for is_small_heap_type, representation is unique
            while h and removed_markers[h[0]] > 0:
                item_repr = heapq.heappop(h)
                removed_markers[item_repr] -= 1

        def _balance_heaps():
            nonlocal s_sum_active, s_cnt_active, l_sum_active, l_cnt_active

            s_target_cnt = (x + 1) // 2

            while s_cnt_active > s_target_cnt:
                _clean_heap_top(small_h)
                if not small_h:
                    break

                s_item_repr = heapq.heappop(small_h)
                val, o_idx = -s_item_repr[0], s_item_repr[1]

                s_sum_active -= val
                s_cnt_active -= 1
                value_locations.pop((val, o_idx))   # Conceptually remove from small_h

                l_item_repr = (val, o_idx)
                heapq.heappush(large_h, l_item_repr)
                value_locations[(val, o_idx)] = 1   # Conceptually add to large_h
                l_sum_active += val
                l_cnt_active += 1

            while s_cnt_active < s_target_cnt:
                _clean_heap_top(large_h)
                if not large_h:
                    break

                l_item_repr = heapq.heappop(large_h)
                val, o_idx = l_item_repr[0], l_item_repr[1]

                l_sum_active -= val
                l_cnt_active -= 1
                value_locations.pop((val, o_idx))

                s_item_repr = (-val, o_idx)
                heapq.heappush(small_h, s_item_repr)
                value_locations[(val, o_idx)] = 0
                s_sum_active += val
                s_cnt_active += 1

            _clean_heap_top(small_h)
            _clean_heap_top(large_h)

        def _add_val_to_window(val, o_idx):
            nonlocal s_sum_active, s_cnt_active, l_sum_active, l_cnt_active
            _clean_heap_top(small_h)
            _clean_heap_top(large_h)    # Clean both before deciding

            # Decide which heap to add to based on current median estimate
            if not small_h or val <= -small_h[0][0]:
                heapq.heappush(small_h, (-val, o_idx))
                value_locations[(val, o_idx)] = 0
                s_sum_active += val
                s_cnt_active += 1
            else:
                heapq.heappush(large_h, (val, o_idx))
                value_locations[(val, o_idx)] = 1
                l_sum_active += val
                l_cnt_active += 1
            _balance_heaps()

        def _remove_val_from_window(val, o_idx):
            nonlocal s_sum_active, s_cnt_active, l_sum_active, l_cnt_active

            # Should not happen if logic is correct
            if (val, o_idx) not in value_locations:
                return
            heap_idx = value_locations.pop((val, o_idx))

            if heap_idx == 0:
                s_sum_active -= val
                s_cnt_active -= 1
                removed_markers[(-val, o_idx)] += 1
            else:
                l_sum_active -= val
                l_cnt_active -= 1
                removed_markers[(val, o_idx)] += 1
            _balance_heaps()

        # Cost calculation phase
        if x == 0:  # Constraint x >= 2
            return 0
        for i in range(n - x + 1):
            _clean_heap_top(small_h)
            _clean_heap_top(large_h)

            current_med_cost = 0
            if x % 2 == 1:
                if not small_h: # Should not happen if x > 0
                    costs[i] = float('inf') # Or handle error
                    continue
                median = -small_h[0][0]
                current_med_cost = (l_sum_active - s_sum_active + median)
            else:
                current_med_cost = (l_cnt_active - s_sum_active)
            costs[i] = current_med_cost

            if i < (n - x):
                _remove_val_from_window(nums[i], i)
                _add_val_to_window(nums[i + x], i + x)

        # DP phase
        dp_prev = [float('inf')] * (n - x + 1)
        dp_curr = [float('inf')] * (n - x + 1)

        for j in range(n - x + 1):
            dp_prev[j] = costs[j]

        if k == 1:
            min_ops = min(dp_prev) if dp_prev else float('inf')
            return int(min_ops) if min_ops != float('inf') else 0

        for c_count in range(2, k + 1):
            min_p_idx_for_prev_block = (c_count - 2) * x
            dq = deque()
            p_ptr_for_dq = min_p_idx_for_prev_block
            min_j_idx = (c_count - 1) * x

            for j in range(min_j_idx, n - x + 1):
                upper_p_bound_in_window = j - x
                while p_ptr_for_dq <= upper_p_bound_in_window:
                    if dp_prev[p_ptr_for_dq] != float('inf'):
                        while dq and dq[-1][0] >= dp_prev[p_ptr_for_dq]:
                            dq.pop()
                        dq.append((dp_prev[p_ptr_for_dq], p_ptr_for_dq))
                    p_ptr_for_dq += 1

                while dq and dq[0][1] < min_p_idx_for_prev_block:
                    dq.popleft()

                if dq:
                    min_val_from_prev_step = dq[0][0]
                    if costs[j] != float('inf'):
                        dp_curr[j] = costs[j] + min_val_from_prev_step

            dp_prev, dp_curr = dp_curr, dp_prev
            for i_fill in range(len(dp_curr)):
                dp_curr[i_fill] = float('inf')

        min_total_ops = min(dp_prev) if dp_prev else float('inf')
        return int(min_total_ops) if min_total_ops != float('inf') else 0