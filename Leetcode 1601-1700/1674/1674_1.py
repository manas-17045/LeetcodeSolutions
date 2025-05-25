# Leetcode 1674: Minimum Moves to make Array Complementary
# https://leetcode.com/problems/minimum-moves-to-make-array-complementary/
# Solved on 25th of May, 2025

class Solution:
    def minMoves(self, nums: list[int], limit: int) -> int:
        """
        Calculates the minimum number of moves required to make all pairs of elements
        (nums[i], nums[n-1-i]) in the array complementary with respect to a target sum S,
        where 1 <= nums[i] <= limit.

        A pair (a, b) is complementary with respect to S if a + b = S.
        A move consists of changing one element in the array to any value between 1 and limit.

        Args:
            nums: The input array of integers.
            limit: The upper bound for the values in the array after moves.

        Returns:
            The minimum number of moves to make all pairs complementary for some target sum S.
        """
        n = len(nums)

        # delta_arr[s] stores the aggregated change in number of moves when the target sum transitions
        # past s-1 to s. It's an event-point array for a sweep-line algorithm.
        # current_total_delta_from_baseline = sum(delta_arr[k] for k up to s).
        # The actual number of moves for a target sum 's' is N (baseline) + current_total_delta_from_baseline.

        # Max possible sum S is limit + limit = 2 * limit.
        # delta_arr needs to cover indices up to 2 * limit + 1 for updates (e.g. y + limit + 1).
        # So, its size should be (2 * limit + 1) + 1 = 2 * limit + 2.
        # Indices used will be from 2 to 2*limit+1.
        delta_arr = [0] * (2 * limit + 2)

        # Iterate through each pair (nums[i], nums[n-1-i]).
        # Let the pair be (a, b). Define x = min(a,b) and y = max(a,b).
        #
        # Baseline assumption: For any target sum S, it takes 2 moves to make a+b=S for this pair.
        # This contributes 2 to the total moves for this pair.
        # So, the overall baseline for N/2 pairs is N moves (since N is total elements, N/2 pairs).
        #
        # Adjustments to this baseline: 1. If S is in the range [x+1, y+limit]: It's possible to achieve sum S with 1
        # move (by changing one element, while the other is x or y). This is a reduction of 1 move (from 2 to 1) for
        # this pair for sums in this range. In delta_arr: delta_arr[x+1] decreases by 1. When S > y+limit,
        # this effect stops, so delta_arr[y+limit+1] increases by 1.
        #
        # 2. If S is exactly x+y: It's possible to achieve sum S with 0 moves (elements already sum to S). This is a
        # further reduction of 1 move (from 1 to 0) for this pair, only for S = x+y. (Note: x+y is always within [
        # x+1, y+limit] because 1<=x<=y<=limit). In delta_arr: delta_arr[x+y] decreases by 1. When S > x+y,
        # this specific effect stops, so delta_arr[x+y+1] increases by 1.
        for i in range(n // 2):
            a = nums[i]
            b = nums[n - 1 - i]
            x = min(a, b)
            y = max(a, b)

            # Effect of rule 1: For S in [x+1, y+limit], cost for this pair is 1 (saves 1 move from baseline 2).
            # Mark start of range S = x+1: cost reduces by 1.
            delta_arr[x + 1] -= 1
            # Mark end of range S = y+limit: cost goes back up by 1 (from 1 to 2) when S becomes y+limit+1.
            delta_arr[y + limit + 1] += 1

            # Effect of rule 2: For S = x+y, cost for this pair is 0 (saves 1 more move from current 1).
            # Mark S = x+y: cost reduces by 1.
            delta_arr[x + y] -= 1
            # Mark S = x+y+1: cost goes back up by 1 (from 0 to 1).
            delta_arr[x + y + 1] += 1

        # Sweep through all possible target sums S.
        # S can range from 1+1=2 to limit+limit=2*limit.

        # min_total_moves is initialized to n. This is the cost if, for a chosen S,
        # all pairs require 2 moves (i.e., current_adjustment is 0 for that S).
        # It also serves as an initial upper bound for the minimum moves.
        min_total_moves = n

        # current_adjustment accumulates the sum of delta_arr[k] for k <= s.
        # It represents the total change from the baseline N for sum s.
        current_adjustment = 0

        # Iterate S from 2 up to 2 * limit (inclusive).
        for s in range(2, 2 * limit + 1):
            current_adjustment += delta_arr[s]
            # Total moves for target sum 's' is: N (baseline) + current_adjustment
            cost_for_s = n + current_adjustment
            if cost_for_s < min_total_moves:
                min_total_moves = cost_for_s

        return min_total_moves