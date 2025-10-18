# Leetcode 2972: Count the Number of Incremovable Subarrays II
# https://leetcode.com/problems/count-the-number-of-incremovable-subarrays-ii/
# Solved on 18th of October, 2025
class Solution:
    def incremovableSubarrayCount(self, nums: list[int]) -> int:
        """
        Counts the number of incremovable subarrays in a given array.
        An incremovable subarray is a subarray such that if it's removed, the remaining elements form a strictly increasing sequence.

        Args:
            nums: A list of integers.
        Returns:
            The total count of incremovable subarrays.
        """
        n = len(nums)

        left = 0
        while left + 1 < n and nums[left] < nums[left + 1]:
            left += 1

        if left == n - 1:
            return (n * (n + 1)) // 2

        right = n - 1
        while right > 0 and nums[right - 1] < nums[right]:
            right -= 1

        totalCount = 0
        suffixStartPointer = right

        for i in range(left + 2):
            prefixEndValue = nums[i - 1] if i > 0 else -float('inf')

            while suffixStartPointer < n and prefixEndValue >= nums[suffixStartPointer]:
                suffixStartPointer += 1

            removalStartPointer = i

            validSuffixStartIndex = max(suffixStartPointer, removalStartPointer + 1)

            if validSuffixStartIndex <= n:
                totalCount += (n - validSuffixStartIndex + 1)

        return totalCount