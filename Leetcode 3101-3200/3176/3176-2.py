# Leetcode 3176: Find the Maximum Length of a Good Subsequence I
# https://leetcode.com/problems/find-the-maximum-length-of-a-good-subsequence-i/
# Solved on 26th of September, 2025
class Solution:
    def maximumLength(self, nums: list[int], k: int) -> int:
        """
        Calculates the maximum length of a subsequence where the number of differing adjacent elements
        is at most k.

        Args:
            nums (list[int]): The input list of integers.
            k (int): The maximum allowed number of "bad" transitions (adjacent differing elements).

        Returns:
            int: The maximum length of such a subsequence.
        """
        n = len(nums)
        if n == 0:
            return 0

        # Initialize dp: list of dicts for t = 0...k
        dp = [dict() for _ in range(k + 1)]
        max_len = 0

        for x in nums:
            # Snapshot to avoid using updates from the same element
            old_dp = [d.copy() for d in dp]

            # Starting new subsequence with just x (0 bad transitions)
            if dp[0].get(x, 0) < 1:
                dp[0][x] = 1
                max_len = max(max_len, 1)

            # Try to extend every previous subsequence
            for t in range(k + 1):
                for val, length in old_dp[t].items():
                    if val == x:
                        # Continuing with same value doesn't increase bad transitions'
                        new_len = length + 1
                        if dp[t].get(x, 0) < new_len:
                            dp[t][x] = new_len
                            if new_len > max_len:
                                max_len = new_len
                    else:
                        # Different value -> consumes one bad transition
                        if t + 1 <= k:
                            new_len = length + 1
                            if dp[t + 1].get(x, 0) < new_len:
                                dp[t + 1][x] = new_len
                                if new_len > max_len:
                                    max_len = new_len

        return max_len