# Leetcode 3566: Partition Array into Two Equal Product Subsets
# https://leetcode.com/problems/partition-array-into-two-equal-product-subsets/
# Solved on 3rd of December, 2025
class Solution:
    def chckEqualPartitions(self, nums: list[int], target: int) -> bool:
        """
        Checks if the given array `nums` can be partitioned into two subsets such that the product of elements
        in each subset is equal to `target`.

        :param nums: A list of integers.
        :param target: The target product for each subset.
        :return: True if such a partition is possible, False otherwise.
        """
        totalProduct = 1
        for num in nums:
            totalProduct *= num

        if totalProduct != target * target:
            return False

        nums.sort(reverse=True)
        length = len(nums)

        def canPartition(index, currentProduct):
            if currentProduct == target:
                return True
            if currentProduct > target or index == length:
                return False

            if canPartition(index + 1, currentProduct * nums[index]):
                return True

            if canPartition(index + 1, currentProduct):
                return True

            return False

        return canPartition(0, 1)