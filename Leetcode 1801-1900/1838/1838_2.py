# Leetcode 1838: Frequency of the Most Frequent Element
# https://leetcode.com/problems/frequency-of-the-most-frequent-element/
# Solved on 5th of August, 2025
class Solution:
    def maxFrequency(self, nums: list[int], k: int) -> int:
        """
        Calculates the maximum frequency of an element in `nums` such that the total operations
        to make all elements in a subarray equal to the largest element in that subarray
        is at most `k`.

        :param nums: A list of integers.
        :param k: The maximum number of operations allowed.
        :return: The maximum possible frequency.
        """
        # Sort nums to try to make smaller elements equal to larger ones
        nums.sort()
        left = 0
        total = 0   # Sum of elements in the current window
        res = 1

        for right, x in enumerate(nums):
            total += x

            while (right - left + 1) * x - total > k:
                total -= nums[left]
                left += 1

            res = max(res, right - left + 1)

        return res