# Leetcode 2835: Minimum Operations to Form Subsequence With Target Sum
# https://leetcode.com/problems/minimum-operations-to-form-subsequence-with-target-sum/
# Solved on 18th of June, 2025

class Solution:
    def minOperations(self, nums: list[int], target: int) -> int:
        """
        Calculates the minimum number of operations to form a subsequence with a target sum.

        An operation consists of splitting a number 2^x into two numbers 2^(x-1).

        Args:
            nums: A list of integers, where each integer is a power of 2.
            target: The target sum.

        Returns:
            The minimum number of operations required to form a subsequence that sums to
            the target. Returns -1 if it's impossible to form the target sum.

        The approach is greedy, processing bits of the target from least significant
        to most significant. For each bit i of the target:
        1. If the i-th bit is set, we need a 2^i.
           - If we have a 2^i available, use it.
           - If not, find the smallest available power 2^j (j > i), break it down
             to get a 2^i, and count the operations.
        2. Carry over any pairs of 2^i as a single 2^(i+1) for the next iteration.
        """
        totalSum = sum(nums)
        if totalSum < target:
            return -1

        # Max power in nums is 30. Max sum is ~1000 * 2^30 ~= 2^40.
        # Target is < 2^31. A count array up to 60 is safe.
        counts = [0] * 60
        for num in nums:
            power = num.bit_length() - 1
            counts[power] += 1

        operations = 0

        # Iterate from the least significant bit upwards.
        for i in range(len(counts) - 1):
            # Check if the i-th bit of target is set.
            if (target >> i) & 1:
                # If we need a 2^i.
                if counts[i] > 0:
                    # Use an available 2^i.
                    counts[i] -= 1
                else:
                    # No 2^i available, must break a larger power.
                    # Find the smallest available power 2^j where j > i.
                    j = i + 1
                    while j < len(counts) and counts[j] == 0:
                        j += 1

                    # This search is guaranteed to succeed due to the initial sum check.

                    # Cost to break 2^j down to 2^i is (j - i).
                    operations += j - i

                    # We've used one 2^j.
                    counts[j] -= 1

                    # The breakdown creates one of each intermediate power.
                    for k in range(i, j):
                        counts[k] += 1

                    # Use the newly created 2^i for the target
                    counts[i] -= 1

            # Carry over pairs o 2^i as single 2^(i + 1).
            counts[i + 1] = counts[i] // 2

        if counts[len(counts) - 1] < (target >> (len(counts) - 1)):
            return -1

        return operations