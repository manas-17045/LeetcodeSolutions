# Leetcode 2740: Find the Value of the Partition
# https://leetcode.com/problems/find-the-value-of-the-partition/
# Solved on 8th of January, 2026
class Solution:
    def findValueOfPartition(self, nums: list[int]) -> int:
        """
        Finds the minimum possible value of a partition.

        Args:
            nums (list[int]): A list of integers.
        Returns:
            int: The minimum value of a partition.
        """
        nums.sort()
        minVal = nums[1] - nums[0]
        for i in range(len(nums) - 1):
            diff = nums[i + 1] - nums[i]

            if diff < minVal:
                minVal = diff

        return minVal