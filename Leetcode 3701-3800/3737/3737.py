# Leetcode 3737: Count Subarrays With Majority Element I
# https://leetcode.com/problems/count-subarrays-with-majority-element-i/
# Solved on 19th of November, 2025
class Solution:
    def countMajoritySubarrays(self, nums: list[int], target: int) -> int:
        """
        Counts the number of subarrays where the `target` element is the majority element.

        Args:
            nums: A list of integers.
            target: The integer to check for majority.
        Returns:
            The number of subarrays where `target` is the majority element.
        """

        totalCount = 0
        n = len(nums)
        for i in range(n):
            currentBalance = 0
            for j in range(i, n):
                if nums[j] == target:
                    currentBalance += 1
                else:
                    currentBalance -= 1

                if currentBalance > 0:
                    totalCount += 1

        return totalCount