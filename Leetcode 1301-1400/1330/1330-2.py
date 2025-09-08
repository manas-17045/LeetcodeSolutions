# Leetcode 1330: Reverse Subarray To Maximize Array Value
# https://leetcode.com/problems/reverse-subarray-to-maximize-array-value/
# Solved on 8th of September, 2025
class Solution:
    def maxValueAfterReverse(self, nums: list[int]) -> int:
        """
        Calculates the maximum possible value of the array sum after reversing at most one subarray.
        :param nums: A list of integers.
        :return: The maximum possible sum of |nums[i] - nums[i+1]| for all i, after one reversal.
        """
        n = len(nums)
        if n < 2:
            return 0

        # Baseline value
        base = 0
        for i in range(n - 1):
            base += abs(nums[i] - nums[i + 1])

        # Best improvement by reversing a prefix (touches left end)
        best_left = 0
        for j in range(n - 1):
            candidate = abs(nums[0] - nums[j + 1]) - abs(nums[j] - nums[j + 1])
            if candidate > best_left:
                best_left = candidate

        # Best improvement by reversing a suffix (touches right end)
        best_right = 0
        for i in range(1, n):
            candidate = abs(nums[i - 1] - nums[-1]) - abs(nums[i - 1] - nums[i])
            if candidate > best_right:
                best_right = candidate

        # Best improvement by reversing some interior subarray
        min_large = 10**10
        max_small = -10**10
        for i in range(n - 1):
            a, b = nums[i], nums[i + 1]
            large = max(a, b)
            small = min(a, b)
            if large < min_large:
                min_large = large
            if small > max_small:
                max_small = small

        best_interior = 0
        if max_small > min_large:
            best_interior = 2 * (max_small - min_large)

        best_gain = max(best_left, best_right, best_interior)
        return base + best_gain