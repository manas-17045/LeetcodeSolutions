# Leetcode 2294: Partition Array Such That Maximum Difference is K
# https://leetcode.com/problems/partition-array-such-that-maximum-difference-is-k/
# Solved on 19th of June, 2025

class Solution:
    def partitionArray(self, nums: list[int], k: int) -> int:
        """
        Partitions an array into the minimum number of subsequences such that the difference between the maximum and minimum element in each subsequence is at most k.

        Args:
            nums: A list of integers.
            k: The maximum allowed difference within a subsequence.

        Returns:
            The minimum number of subsequences.
        """
        if not nums:
            return 0

        nums.sort()
        count = 1
        startVal = nums[0]

        for x in nums[1:]:
            # If this element can't fit in the current subsequence, start a new one
            if x - startVal > k:
                count += 1
                startVal = x

        return count