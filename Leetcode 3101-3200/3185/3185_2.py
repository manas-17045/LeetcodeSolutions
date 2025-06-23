# Leetcode 3185: Count Pairs That Form a Complete Day II
# https://leetcode.com/problems/count-pairs-that-form-a-complete-day-ii/
# Solved on 23rd of June, 2025
class Solution:
    def countCompleteDayPairs(self, hours: list[int]) -> int:
        """
        Counts the number of complete day pairs from a list of hours.

        A complete day pair (i, j) is a pair of indices such that
        hours[i] + hours[j] is a multiple of 24.

        Args:
            hours: A list of integers representing hours.

        Returns:
            The total number of complete day pairs.
        """
        # Count how many times each remainder mod 24 appears
        cnt = [0] * 24
        for h in hours:
            cnt[h % 24] += 1

        total = 0

        # Pairs where both have remainder 0 -> choose(cnt[0], 2)
        total += cnt[0] * (cnt[0] - 1) // 2

        # If 24 is even, remainder 12 pairs with itself as well
        total += cnt[12] * (cnt[12] - 1) // 2

        # For 1 <= r < 12, pair r with 24 - r
        for r in range(1, 12):
            total += cnt[r] * cnt[24 - r]

        return total