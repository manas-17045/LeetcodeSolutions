# Leetcode 1931: Painting a Grid With Three Different Colors
# https://leetcode.com/problems/painting-a-grid-with-three-different-colors/
# Solved on 18th of May, 2025

class Solution:
    def colorTheGrid(self, m: int, n: int) -> int:
        """
        Calculates the number of ways to color an m x n grid with three colors such that no two adjacent cells have
        the same color.

        Args:
            m: The number of rows in the grid.
            n: The number of columns in the grid.

        Returns:
            The number of valid colorings modulo 10^9 + 7.

        Constraints:
            1 <= m <= 5
            1 <= n <= 1000
        """
        MOD = 10**9 + 7

        # Generate all valid colorings for a single column of height m
        valid_single_column_patterns = []

        def generate_patterns_recursive(row_idx: int, current_pattern_tuple: tuple):
            if row_idx == m:
                valid_single_column_patterns.append(current_pattern_tuple)
                return

            # Colors are represented as 0, 1, 2
            for color_val in range(3):
                # Check adjacency with the cell above in the same column
                if row_idx > 0 and color_val == current_pattern_tuple[row_idx - 1]:
                    continue    # Conflict with the cell above, try next color

                # If no conflict, recurse for the next one
                generate_patterns_recursive(row_idx + 1, current_pattern_tuple + (color_val,))

        generate_patterns_recursive(0, tuple())

        num_valid_patterns = len(valid_single_column_patterns)
        if num_valid_patterns == 0: # Should not happen for m >= 1
            return 0

        # Precompute compatibility between patterns for adjacent columns
        # compatible_transitions[next_pattern_idx] = list of prev_pattern_idx that can provide next_pattern
        compatible_transitions = [[] for _ in range(num_valid_patterns)]

        for prev_idx in range(num_valid_patterns):
            prev_pattern = valid_single_column_patterns[prev_idx]
            for next_idx in range(num_valid_patterns):
                next_pattern = valid_single_column_patterns[next_idx]

                is_compatible = True
                # Check all cells in the column
                for r in range(m):
                    # Horizontal conflict
                    if prev_pattern[r] == next_pattern[r]:
                        is_compatible = False
                        break

                if is_compatible:
                    # If prev_pattern can be to the left of next_pattern,
                    # add prev_idx to the list of compatible predecessors for next_idx.
                    compatible_transitions[next_idx].append(prev_idx)

        # ---- Dynamic Programming ---- dp_prev[pattern_idx] = number of ways to color up to the previous column (col
        # - 1), such that column (col - 1) has `pattern_idx`.
        # Initialize for the first column (column 0).
        # Each valid pattern can be the first column in exactly 1 way.
        dp_prev = [1] * num_valid_patterns

        # Iterate for columns from the second column (index 1) up to the n-th column (index n - 1)
        for _col_num in range(1, n):
            # DP states for the current column
            dp_curr = [0] * num_valid_patterns
            for next_pattern_idx in range(num_valid_patterns):
                sum_ways_for_this_next_pattern = 0
                # Sum ways from compatible previous column patterns
                for prev_pattern_idx in compatible_transitions[next_pattern_idx]:
                    sum_ways_for_this_next_pattern = (sum_ways_for_this_next_pattern + dp_prev[prev_pattern_idx]) % MOD

                dp_curr[next_pattern_idx] = sum_ways_for_this_next_pattern

            # Current column's states become previous for the next iteration
            dp_prev = dp_curr

        # Final result is the sum of ways for the last column (column (n - 1))
        total_ways = sum(dp_prev) % MOD
        return total_ways