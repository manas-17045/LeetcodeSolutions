# Leetcode 3398: Smallest Substring With Identical Characters I
# https://leetcode.com/problems/smallest-substring-with-identical-characters-i/
# Solved on 29th May, 2025

class Solution:
    def minLength(self, s: str, numOps: int) -> int:
        """
        Finds the minimum possible length of the longest identical consecutive substring in a binary string `s`
        after performing at most `numOps` operations. An operation consists of flipping a character ('0' to '1' or '1' to '0').

        The problem is solved using binary search on the possible values of the maximum allowed length of an identical
        substring. For a given maximum length `k_val`, a dynamic programming approach is used to check if it's possible
        to transform the string `s` such that no identical consecutive substring has a length greater than `k_val`
        using at most `numOps` operations.

        Args:
            s: The input binary string.
            numOps: The maximum number of operations allowed.

        Returns:
            The minimum possible length of the longest identical consecutive substring.
        """
        n = len(s)

        # A large value for infinity. Maximum possible operations can be n.
        # Using math.inf is also an option. n + 2 ensures it's larger than any valid sum of ops.
        infinity = n + 2

        # check(k_val) returns True if it's possible to make the longest
        # identical substring have length at most k_val with at most numOps.
        def check(k_val: int) -> bool:
            # Smallest possible length for a non-empty string's substring is 1.
            # k_val = 0 is not a valid maximum length for this problem.
            # The binary search should ensure k_val >= 1.
            if k_val == 0:
                return False

            # dp[streak_len][char_val]
            # Stores min ops for the prefix processed so far, ending with streak_len of char_val.
            # streak_len is 1-indexed, up to k_val. dp[j][0] for '0', dp[j][1] for '1'.
            # Array size is (k_val + 1) to use 1-based indexing for streak_len.
            prev_dp = [[infinity] * 2 for _ in range(k_val + 1)]

            # Base case for s[0] (prefix of length 1 ending at s[0])
            # Cost to make s[0] '0'
            cost_s0_eq_0 = 1 if s[0] == '1' else 0
            prev_dp[1][0] = cost_s0_eq_0
            # Cost to make s[0] '1'
            cost_s0_eq_1 = 1 if s[0] == '0' else 0
            prev_dp[1][1] = cost_s0_eq_1

            # Iterate for characters s[1] through s[n - 1]
            # The loop process characters from the second (index 1) to the last (index n - 1).
            for i in range(1, n):   # current char under consideration is s[i]
                current_dp = [[infinity] * 2 for _ in range(k_val + 1)]

                # Calculate min_ops_ending_prev_with_0 and min_ops_ending_with_prev_with_1
                # These are minimum operations for prefix s[0...i - 1] ending with '0' or '1' respectively,
                # with any valid streak length (1 to k_val).
                min_ops_ending_prev_with_0 = infinity
                min_ops_ending_prev_with_1 = infinity
                # Iterate through possible streak lengths for s[i - 1]
                for streak_idx in range(1, k_val + 1):
                    min_ops_ending_prev_with_0 = min(min_ops_ending_prev_with_0, prev_dp[streak_idx][0])
                    min_ops_ending_prev_with_1 = min(min_ops_ending_prev_with_1, prev_dp[streak_idx][1])

                # Consider making s[i] be current_char_val (0 or 1)
                for current_char_val in range(2):   # 0 or 1
                    cost_to_make_si_current_char_val = 1 if int(s[i]) != current_char_val else 0

                    # Streak of length 1 for current_char_val at s[i]
                    # This means s[i - 1] must have been (1 - current_char_val).
                    min_prev_ops_for_opposite_char: int
                    if current_char_val == 0:
                        # s[i] is '0', so s[i - 1] was '1'
                        min_prev_ops_for_opposite_char = min_ops_ending_prev_with_1
                    else:
                        # s[i] is '1', so s[i - 1] was '0'
                        min_prev_ops_for_opposite_char = min_ops_ending_prev_with_0

                    if min_prev_ops_for_opposite_char != infinity:
                        current_dp[1][current_char_val] = min_prev_ops_for_opposite_char + cost_to_make_si_current_char_val

                    # Streak of length > 1 for current_char_val at s[i]
                    # This means s[i - 1] must have been current_char_val.
                    # The streak ending at s[i] would be `streak_len_at_i`.
                    # the streak ending at s[i - 1] (which was current_char_val) would be `streak_len_at_i - 1`.
                    for streak_len_at_i in range(2, k_val + 1):
                        cost_from_prev_streak = prev_dp[streak_len_at_i - 1][current_char_val]
                        if cost_from_prev_streak != infinity:
                            current_dp[streak_len_at_i][current_char_val] = cost_from_prev_streak + cost_to_make_si_current_char_val

                # Move current_dp to prev_dp for the next iteration
                prev_dp = current_dp

            # After processing all characters, find the overall minimum operations for string s
            min_total_ops_for_s = infinity
            for streak_len_final in range(1, k_val + 1):
                min_total_ops_for_s = min(min_total_ops_for_s, prev_dp[streak_len_final][0], prev_dp[streak_len_final][1])

            return min_total_ops_for_s <= numOps

        # Binary search for the smallest k_val (the answer)
        low = 1     # Smallest possible max length is 1
        high = n    # Largest possible max length is n
        ans = n     # Initialize `ans` with the largest possible value (worst case)

        while low <= high:
            mid = (low + high) // 2     # Candidate for the max length

            if check(mid):  # If it;s possible to achieve max length `mid`
                ans = mid   # `mid` is a possible answer, try for an even smaller length
                high = mid - 1
            else:   # Not possible to achieve max length `mid` with numOps
                low = mid + 1   # Need to allow longer streaks. so increase mid

        return ans