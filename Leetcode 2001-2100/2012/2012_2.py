# Leetcode 2012: Sum of Beauty in the Array
# https://leetcode.com/problems/sum-of-beauty-in-the-array/
# Solved on 28th of June, 2025
class Solution:
    def sumBeauties(self, nums: list[int]) -> int:
        """
        Calculates the sum of "beauties" for elements in a given list `nums`.

        An element `nums[i]` (where 1 < i < n - 1) is considered:
        - "beautiful" with a score of 2 if `nums[j] < nums[i] < nums[k]` for all `j < i` and all `k > i`.
        - "beautiful" with a score of 1 if `nums[i-1] < nums[i] < nums[i+1]`.

        The function returns the total sum of these beauty scores.
        """
        n = len(nums)
        # Build suffix_min
        suffix_min = [0] * n
        INF = 10**9 + 5
        suffix_min[n - 1] = INF
        for i in range((n - 2), -1, -1):
            # The smallest element to the right of i is either
            # nums[i + 1] or the smallest to the right of (i + 1).
            suffix_min[i] = min(suffix_min[i + 1], nums[i + 1])

        beauty_sum = 0
        left_max = nums[0]  # Max of nums[0...(i - 1)] at each i

        # Iterate only over i = 1...(n - 2)
        for i in range(1, (n - 1)):
            x = nums[i]
            if left_max < x < suffix_min[i]:
                beauty_sum += 2
            elif nums[i - 1] < x < nums[i + 1]:
                beauty_sum += 1

            # Update prefix max for next iteration
            left_max = max(left_max, x)

        return beauty_sum