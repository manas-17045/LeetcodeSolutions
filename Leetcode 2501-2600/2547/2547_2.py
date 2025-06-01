# Leetcode 2547: Minimum Cost to Split an Array
# https://leetcode.com/problems/minimum-cost-to-split-an-array/
# Solved on 1st of June, 2025
import sys


class Solution:
    def minCost(self, nums: list[int], k: int) -> int:
        """
        Calculates the minimum cost to split the array `nums` into several subarrays.

        The cost of splitting the array is the sum of the costs of each subarray.
        The cost of a subarray is defined as `k + trimmed_length`, where `trimmed_length`
        is the number of elements in the subarray that appear more than once.

        This solution uses dynamic programming. `dp[i]` represents the minimum cost
        to split the prefix `nums[0:i]`. The transition considers all possible
        last subarrays ending at index `i-1`.

        Args:
            nums: A list of integers.
            k: An integer representing the base cost for each subarray.

        Returns:
            The minimum cost to split the array `nums`.
        """
        n = len(nums)
        if n == 0:
            return 0

        # Since 0 >= nums[i] < n by constraints, we can size the frequency array to n.
        # If you want to guard against out-of-range values in nums when testing,
        # replace `m = n` with `m = max(nums) + 1`.
        m = n

        # dp[i] = minimum cost to split nums[0:i]
        dp = [0] + [sys.maxsize] * n

        for i in range(1, n + 1):
            freq = [0] * m
            duplicates = 0

            # Build subarrays ending at index i - 1, starting from j and going downward.
            # We keep track of how many "duplicate" occurrences are in nums[j:i].
            for j in range(i - 1, -1, -1):
                v = nums[j]

                # If this is the second time v appears, we add 2 to duplicates
                # (because both occurrences now count toward trimmed length).
                if freq[v] == 1:
                    duplicates += 2
                # If v has appeared more than once already, each additional occurrence
                # contributes exactly 1 more to the trimmed length.
                elif freq[v] > 1:
                    duplicates += 1

                freq[v] += 1

                # Cost of taking subarray nums[j:i] in a single chunk:
                # k for the base cost + duplicates for the trimmed length
                costSubarray = k + duplicates

                # Transition: dp[i] = min over j of (dp[j] + cost of nums[j:i])
                dp[i] = min(dp[i], dp[j] + costSubarray)

        return dp[n]