# Leetcode 3101: Count Alternating Subarrays
# https://leetcode.com/problems/count-alternating-subarrays/
# Solved on 5th of December, 2025
class Solution:
    def countAlternatingSubarrays(self, nums: list[int]) -> int:
        """
        Counts the number of alternating subarrays in the given list of integers.

        Args:
            nums: A list of integers (0s and 1s).
        Returns:
            The total count of alternating subarrays.
        """
        totalCount = 1
        currentLength = 1

        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                currentLength += 1
            else:
                currentLength = 1

            totalCount += currentLength

        return totalCount