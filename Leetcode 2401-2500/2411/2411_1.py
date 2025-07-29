# Leetcode 2411: Smallest Subarrays With Maximum Bitwise OR
# https://leetcode.com/problems/smallest-subarrays-with-maximum-bitwise-or/
# Solved on 29th of July, 2025
class Solution:
    def smallestSubarrays(self, nums: list[int]) -> list[int]:
        """
        Finds the smallest subarray for each index `i` such that the bitwise OR of all elements
        in that subarray (starting at `i`) is maximized.

        Args:
            nums: A list of integers.
        Returns:
            A list of integers, where `answer[i]` is the length of the smallest subarray starting at `i`
            that achieves the maximum possible bitwise OR value.
        """
        numCount = len(nums)
        answer = [0] * numCount
        lastSeen = [0] * 32

        for i in range((numCount - 1), -1, -1):
            for j in range(32):
                if (nums[i] >> j) & 1:
                    lastSeen[j] = i

            endIndex = i
            for index in lastSeen:
                endIndex = max(endIndex, index)

            answer[i] = endIndex - i + 1

        return answer