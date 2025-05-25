# Leetcode 1674: Minimum Moves to Make Aray Complementary
# https://leetcode.com/problems/minimum-moves-to-make-array-complementary/
# Solved on 25th of May, 2025

class Solution:
    def minMoves(self, nums: list[int], limit: int) -> int:
        """
        Calculates the minimum number of moves required to make all pairs of numbers
        in the input array `nums` complementary with respect to the given `limit`.
        A pair (nums[i], nums[n-1-i]) is complementary if their sum equals a target value `t`.
        A move consists of changing one of the numbers in a pair to any value between 1 and `limit`.

        The algorithm uses a difference array approach to efficiently calculate the number of moves
        for each possible target sum.

        Args:
            nums: A list of integers.
            limit: An integer representing the upper bound for the numbers after moves.

        Returns:
            The minimum number of moves required.
        """
        n = len(nums)
        pairs = n // 2

        # diff[t] will accumulate the net change to "subtract 1 move" for sums >= t
        # zero[t] will count how many pairs already sum exactly to t (they need one more subtraction)
        size = 2 * limit + 2
        diff = [0] * size
        zero = [0] * size

        # Base: every pair cost 2 moves for every target sum
        base_moves = pairs * 2

        # Build our range-update and exact-sum counters
        for i in range(pairs):
            a, b = nums[i], nums[n - 1 - i]
            lo = 1 + min(a, b)  # From this sum onward, only 1 move is needed
            hi = limit + max(a, b)  # Up to this sum, only 1 move is needed
            s = a + b   # At this exact sum, 0 moves are needed

            diff[lo] -= 1
            diff[hi + 1] += 1
            zero[s] += 1

        # Sweep through all possible sums to compute total moves
        ans = float('inf')
        curr_sub = 0    # current accumulated "subtract - 1" from diff
        for t in range(2, 2 * limit + 1):
            curr_sub += diff[t]
            # base_moves – 1 for each pair where t∈[lo,hi], and –1 more for each pair with sum==t
            moves = base_moves + curr_sub - zero[t]
            if moves < ans:
                ans = moves

        return ans