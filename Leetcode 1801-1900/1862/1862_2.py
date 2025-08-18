# Leetcode 1862: Sum of Floored Pairs
# https://leetcode.com/problems/sum-of-floored-pairs/
# Solved on 18th of August, 2025
class Solution:
    def sumOfFlooredPairs(self, nums: list[int]) -> int:
        """
        Calculates the sum of floored pairs (nums[i] // nums[j]) for all i, j.

        Args:
            nums: A list of integers.
        Returns:
            The sum of floored pairs modulo 10^9 + 7.
        """
        MOD = 10 ** 9 + 7
        if not nums:
            return 0

        maxA = max(nums)
        freq = [0] * (maxA + 1)
        for v in nums:
            freq[v] += 1

        # prefix count: prefix[i] = number of elements <= i
        prefix = [0] * (maxA + 1)
        running = 0
        for i in range(maxA + 1):
            running += freq[i]
            prefix[i] = running

        ans = 0
        # Iterate possible denominators x
        for x in range(1, maxA + 1):
            if freq[x] == 0:
                continue
            fx = freq[x]
            # Sum over k where y in [k*x, k*x + x - 1]
            for start in range(x, maxA + 1, x):
                k = start // x
                end = start + x - 1
                if end > maxA:
                    end = maxA
                count_in_range = prefix[end] - prefix[start - 1]
                if count_in_range:
                    ans += fx * k * count_in_range
            # Keep ans from growing too large
            ans %= MOD

        return ans % MOD