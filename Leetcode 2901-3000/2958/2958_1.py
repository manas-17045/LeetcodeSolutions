# Leetcode 2958: Length of Longest Subarray With at Most K Frequency
# https://leetcode.com/problems/length-of-longest-subarray-with-at-most-k-frequency/
# Solved on 2nd of July, 2024
class Solution:
    def maxSubarrayLength(self, nums: list[int], k: int) -> int:
        """
        Finds the length of the longest subarray such that the frequency of each element
        in the subarray is at most k.

        Args:
            nums: A list of integers.
            k: The maximum allowed frequency for any element in the subarray.
        """
        counter = {}
        left = 0
        max_len = 0

        for right in range(len(nums)):
            counter[nums[right]] = counter.get(nums[right], 0) + 1

            while counter[nums[right]] > k:
                counter[nums[left]] -= 1
                left += 1

            max_len = max(max_len, right - left + 1)

        return max_len