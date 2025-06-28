# Leetcode 3077: Maximum Strength of K Disjoint Subarrays
# https://leetcode.com/problems/maximum-strength-of-k-disjoint-subarrays/
# Solved on 28th of June, 2025
class Solution:
    def maximumStrength(self, nums: list[int], k: int) -> int:
        """
        Calculates the maximum strength achievable by partitioning the array `nums` into `k` non-empty subarrays.

        The strength is defined as the sum of strengths of individual subarrays.
        The strength of a subarray is its sum multiplied by a coefficient.
        The coefficient for the j-th subarray (1-indexed) is (k - j + 1) if j is odd, and -(k - j + 1) if j is even.

        Args:
            nums: A list of integers representing the input array.
            k: An integer representing the number of subarrays to partition into.

        Returns:
            The maximum possible strength.
        """
        n = len(nums)
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[n + 1] = prefix[i] + nums[i]

        dp_prev = [0] * (n + 1)

        for j in range(1, (k + 1)):
            coeff = (k - j + 1) if (j % 2 == 1) else -(k - j + 1)

            dp_curr = [float("-inf")] * (n + 1)
            best_val = dp_prev[0] - coeff * prefix[0]

            for i in range(1, (n + 1)):
                dp_curr[i] = best_val + coeff * prefix[i]
                # Now, include position i as a candidate for future u
                candidate = dp_prev[i] - coeff * prefix[i]
                if candidate > best_val:
                    best_val = candidate

            dp_prev = dp_curr

        # Answer is the nest over all possible end-positions of the k-th subarray
        return max(dp_prev)