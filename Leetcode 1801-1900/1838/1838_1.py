# Leetcode 1838: Frequency of the Most Frequent Element
# https://leetcode.com/problems/frequency-of-the-most-frequent-element/
# Solved on 5th of August, 2025
class Solution:
    def maxFrequency(self, nums: list[int], k: int) -> int:
        """
        Calculates the maximum possible frequency of an element in the array after performing at most k operations.
        An operation consists of incrementing an element by 1.

        Args:
            nums: A list of integers.
            k: The maximum number of operations allowed.

        Returns:
            The maximum frequency of an element.
        """
        nums.sort()
        left = 0
        currentSum = 0
        maxFrequency = 0

        for right in range(len(nums)):
            currentSum += nums[right]
            while (right - left + 1) * nums[right] - currentSum > k:
                currentSum -= nums[left]
                left += 1
            maxFrequency = max(maxFrequency, right - left + 1)

        return maxFrequency