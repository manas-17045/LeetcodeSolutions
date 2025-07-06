# Leetcode 3194: Minimum Average of Smallest and Largest Elements
# https://leetcode.com/problems/minimum-average-of-smallest-and-largest-elements/
# Solved on 6th of July, 2025
class Solution:
    def minimumAverages(self, nums: list[int]) -> float:
        """
        Calculates the minimum average among pairs formed by the smallest and largest
        elements, moving inwards.

        The problem asks to find the minimum possible average of any pair of elements
        (nums[i], nums[j]) where i != j. However, the problem statement implies a
        specific pairing strategy: after sorting, we pair the smallest with the largest,
        the second smallest with the second largest, and so on. We then find the minimum
        of these specific averages.
        """
        # Sort `nums` in-place
        nums.sort()
        n = len(nums)
        # Initialize min_avg to +infinity
        min_avg = float('inf')
        # Pair smallest with largest, moving inward
        for i in range(n // 2):
            avg = (nums[i] + nums[n - 1 - i]) / 2
            if avg < min_avg:
                min_avg = avg
        return min_avg