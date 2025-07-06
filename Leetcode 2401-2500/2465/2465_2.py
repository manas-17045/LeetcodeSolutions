# Leetcode 2465: Number of Distinct Averages
# https://leetcode.com/problems/number-of-distinct-averages/
# Solved on 6th of July, 2025
class Solution:
    def distinctAverages(self, nums: list[int]) -> int:
        """
        Calculates the number of distinct averages formed by repeatedly
        removing the minimum and maximum elements from the array and
        calculating their average.

        Args:
            nums: A list of integers.
        Returns:
            The number of distinct averages.
        """
        # Sort the list so that pairing min with max is trivial
        nums.sort()
        n = len(nums)
        seen_sums = set()

        # Pair i-th smallest with i-th largest
        for i in range(n // 2):
            total = nums[i] + nums[n - 1 - i]
            seen_sums.add(total)

        # The number of distinct sums == the number of distinct averages.
        return len(seen_sums)