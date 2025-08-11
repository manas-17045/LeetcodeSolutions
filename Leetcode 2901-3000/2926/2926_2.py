# Leetcode 2926: Maximum Balanced Subsequence Sum
# https://leetcode.com/problems/maximum-balanced-subsequence-sum/
# Solved on 11th of August, 2025
import bisect


class Solution:
    def maxBalancedSubsequenceSum(self, nums: list[int]) -> int:
        """
        Calculates the maximum sum of a balanced subsequence.
        A subsequence is balanced if for any two elements nums[i] and nums[j] in the subsequence with i < j,
        nums[j] - nums[i] >= j - i. This can be rewritten as nums[j] - j >= nums[i] - i.
        :param nums: A list of integers.
        :return: The maximum sum of a balanced subsequence.
        """
        n = len(nums)
        if n == 0:
            return 0

        # Compute v[i] = nums[i] - i
        v = [nums[i] - i for i in range(n)]

        # Coordinate compress v-values
        uniq = sorted(set(v))
        m = len(uniq)

        # Fenwick tree (1-indexed) for prefix maximum
        bit = [0] * (m + 1)

        def bit_update(idx: int, val: int) -> None:
            while idx <= m:
                if val > bit[idx]:
                    bit[idx] = val
                idx += idx & -idx

        def bit_query(idx: int) -> int:
            res = 0
            while idx > 0:
                if bit[idx] > res:
                    res = bit[idx]
                idx -= idx & -idx
            return res

        ans = -10**18
        for i in range(n):
            # Compressed position for v[i]
            pos = bisect.bisect_left(uniq, v[i]) + 1
            best_prefix = bit_query(pos)
            # We allow starting a new subsequence at i, so use max(0, best_prefix)
            dp_i = nums[i] + (best_prefix if best_prefix > 0 else 0)
            # Update Fenwick at position pos with dp_i
            bit_update(pos, dp_i)
            if dp_i > ans:
                ans = dp_i

        return ans