# Leetcode 2829: Determine the Minimum Sum of a k-avoiding Array
# https://leetcode.com/problems/determine-the-minimum-sum-of-a-k-avoiding-array/
# Solved on 3rd of September, 2025
class Solution:
    def minimumSum(self, n: int, k: int) -> int:
        """
        Calculates the minimum possible sum of `n` distinct positive integers
        such that no two integers sum up to `k`.
        :param n: The number of distinct positive integers to choose.
        :param k: The forbidden sum for any pair of chosen integers.
        :return: The minimum possible sum.
        """
        chosen: set[int] = set()
        cur = 1
        total = 0
        while len(chosen) < n:
            # If picking cur would create a forbidden pair with an already chosen number, skip it.
            if (k - cur) not in chosen:
                chosen.add(cur)
                total += cur
            cur += 1
        return total