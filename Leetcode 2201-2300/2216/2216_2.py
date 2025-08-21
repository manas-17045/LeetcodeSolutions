# Leetcode 2216: Minimum Deletions to Make Array Beautiful
# https://leetcode.com/problems/minimum-deletions-to-make-array-beautiful/
# Solved on 21st of August, 2025
class Solution:
    def minDeletion(self, nums: list[int]) -> int:
        """
        Deletes the minimum number of elements from the input list `nums` such that the remaining list
        has an even length and no two adjacent elements are equal.

        Args:
            nums (list[int]): The input list of integers.
        Returns:
            int: The minimum number of deletions required.
        """
        n = len(nums)
        count = 0
        # Sentinel value, since nums[i] >= 0
        last = -1

        for num in nums:
            if count % 2 == 0:
                count += 1
                last = num
            elif num != last:
                count += 1
                last = num

        kept = count if count % 2 == 0 else count - 1

        return n - kept