# Leetcode 3177: Find the Maximum Length of a Good Subsequence II
# https://leetcode.com/problems/find-the-maximum-length-of-a-good-subsequence-ii/
# Solved on 11th of August, 2025
from collections import defaultdict


class Solution:
    def maximumLength(self, nums: list[int], k: int) -> int:
        """
        Calculates the maximum length of a subsequence where at most k elements are different from their preceding element.

        Args:
            nums (list[int]): The input list of integers.
            k (int): The maximum allowed number of "different" transitions.
        Returns:
            int: The maximum length of such a subsequence.
        """
        if not nums:
            return 0

        n = len(nums)
        k = min(k, n)

        dp = [defaultdict(int) for _ in range(k + 1)]
        tops = [(0, None, 0) for _ in range(k + 1)]

        best_answer = 0

        for x in nums:
            # Snapshot of tops before this element's updates
            tops_snapshot = list(tops)

            # Compute the new best lengths for ending with x for each t (using snapshot)
            tops_snapshot = list(tops)

            # Compute the new best lengths for ending with x for each t (may be 0)
            new_len_for_t = [0] * (k + 1)
            for t in range(k + 1):
                # Current stored length ending with x (may be 0)
                cur = dp[t].get(x, 0)
                # Keep existing if nothing better
                best_len = cur

                # Extend a subsequence tha already ends with x (no new transition)
                if cur > 0:
                    best_len = max(best_len, (cur + 1))

                # Extend a subsequence that ends with a different value -> uses one more transition
                if t > 0:
                    max1, val1, sec1 = tops_snapshot[t - 1]
                    # Pick best length that does NOT end with x
                    best_other = 0
                    if max1 > 0:
                        if val1 != x:
                            best_other = max1
                        else:
                            best_other = sec1
                    if best_other > 0:
                        best_len = max(best_len, best_other + 1)

                # We can always start a new subsequence of length 1 (uses 0 transitions)
                if t == 0:
                    best_len = max(best_len, 1)

                new_len_for_t[t] = best_len

            # Apply updates to dp and tops using new values (only for value x)
            for t in range(k + 1):
                newV = new_len_for_t[t]
                if newV <= 0:
                    continue
                oldV = dp[t].get(x, 0)
                if newV > oldV:
                    dp[t][x] = newV
                    # Update tops[t] accordingly
                    max1, val1, sec1 = tops[t]
                    if val1 is None:
                        tops[t] = (newV, x, 0)
                    elif val1 == x:
                        # Same value as current top; just update top length
                        tops[t] = (newV if newV > max1 else max1, val1, sec1)
                    else:
                        # New value differs from current top value
                        if newV >= max1:
                            tops[t] = (newV, x, sec1)
                        elif newV > sec1:
                            tops[t] = (max1, val1, newV)
                    if newV > best_answer:
                        best_answer = newV

        return best_answer