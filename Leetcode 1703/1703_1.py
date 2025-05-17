# Leetcode 1703: Minimum Adjacent Swaps for K Consecutive Ones
# https://leetcode.com/problems/minimum-adjacent-swaps-for-k-consecutive-ones/
# Solved on 17th of May, 2025

class Solution:
    def minMoves(self, nums: list[int], k: int) -> int:
        """
        Calculates the minimum number of adjacent swaps required to group k consecutive 1s in a binary array.

        This function transforms the problem into finding a window of size k in a transformed array 'g'
        where elements are as close as possible to the median of that window.  The transformation
        g[i] = one_indices[i] - i accounts for the increasing index offset as we move through the original array.
        Prefix sums are used to efficiently calculate the cost (sum of absolute differences from the median)
        for each window.

        Args:
            nums: A list of integers (0 or 1) representing the binary array.
            k: The number of consecutive 1s to group.

        Returns:
            The minimum number of adjacent swaps needed to group k consecutive 1s.  Returns 0 if k is 1.
        """

        if k == 1:
            return 0

        one_indices = [i for i, num_val in enumerate(nums) if num_val == 1]
        num_ones = len(one_indices)

        # Transformed array g[i] = one_indices[i] - i.
        # The problem reduces to finding a window of k elements in g
        # and making them all equal to the median of that window, minimizing sum of absolute differences.
        g = [one_indices[i] - i for i in range(num_ones)]

        # Prefix sums for g to quickly calculate sum of elements in subsegments.
        # pref_g[i] will store sum g[0]...g[i - 1]. So, pref_g has size num_ones + 1.
        pref_g = [0] * (num_ones + 1)
        for i in range(num_ones):
            pref_g[i + 1] = pref_g[i] + g[i]

        min_total_moves = float('inf')

        # Iterate through all possible windows of size k in g.
        # A window starts at index s and ends at (s + k - 1).
        for s in range(num_ones - k + 1):
            current_window_cost = 0
            if k % 2 == 1:
                # k = 2r + 1. This median elemnt in the window g[s...s + k - 1] is g[s = r].
                r = (k - 1) // 2
                # The median value (target for all g_j in window) is g[s+r].
                # Cost = Sum_{j from s to s+r-1} (g[s+r] - g[j]) + Sum_{j from s+r+1 to s+k-1} (g[j] - g[s+r])
                # This simplifies to (Sum of elements right of median) - (Sum of elements left of median)

                # Sum of g[s...s+r-1] (left part, r elements)
                sum_left_half = pref_g[s + r] - pref_g[s]
                # Sum of g[s+r+1...s+k-1] (right part, r elements)
                sum_right_half = pref_g[s + k] - pref_g[s + r + 1]

                current_window_cost = sum_right_half - sum_left_half

            else:
                # k = 2r. Median can be any value between g[s+r-1] and g[s+r].
                # The minimum sum |g_j - Median| is (Sum of right r elements) - (Sum of left r elements)
                r = k // 2

                # Sum of g[s...s+r-1] (left part, r elements)
                sum_left_half = pref_g[s + r] - pref_g[s]
                # Sum of g[s+r...s+k-1] (right part, r elements)
                sum_right_half = pref_g[s + k] - pref_g[s + r]

                current_window_cost = sum_right_half - sum_left_half

            if current_window_cost < min_total_moves:
                min_total_moves = current_window_cost

        return min_total_moves