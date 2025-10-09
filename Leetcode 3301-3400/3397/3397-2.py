# Leetcode 3397: Maximum Number of Distinct Elements After Operations
# https://leetcode.com/problems/maximum-number-of-distinct-elements-after-operations/
# Solved on 9th of October, 2025
class Solution:
    def maxDistinctElements(self, nums: list[int], k: int) -> int:
        """
        This function aims to find the maximum number of distinct elements that can be formed
        from the given array `nums` such that each chosen element `x` is within `k` distance
        of an original number `num` (i.e., `num - k <= x <= num + k`).

        :param nums: A list of integers.
        :param k: An integer representing the maximum allowed distance.
        :return: The maximum number of distinct elements.
        """
        nums.sort()
        count = 0
        last_assigned = float('-inf')

        for num in nums:
            candidate = max(num - k, last_assigned + 1)

            # Check if candidate is within the valid range [num - k, num + k]
            if candidate <= num + k:
                count += 1
                last_assigned = candidate

        return count