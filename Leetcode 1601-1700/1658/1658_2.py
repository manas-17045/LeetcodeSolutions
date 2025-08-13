# Leetcode 1658: Minimum Operations to Reduce X to Zero
# https://leetcode.com/problems/minimum-operations-to-reduce-x-to-zero/
# Solved on 13th of August, 2025
class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:
        """
        Calculates the minimum number of operations to reduce x to 0.
        An operation consists of removing either the leftmost or rightmost element from the array nums.
        :param nums: A list of integers.
        :param x: The target value to reduce to 0.
        :return: The minimum number of operations, or -1 if it's not possible.
        """
        total = sum(nums)
        target = total - x
        n = len(nums)

        if target < 0:
            return -1

        if target == 0:
            return n

        left = 0
        cur = 0
        # Store length of longest subarray with sum == target
        max_len = -1

        for right in range(n):
            cur += nums[right]
            # Shrink window while sum too large
            while cur > target and left <= right:
                cur -= nums[left]
                left += 1
            # Check equality
            if cur == target:
                max_len = max(max_len, right - left + 1)

        return n - max_len if max_len != -1 else -1