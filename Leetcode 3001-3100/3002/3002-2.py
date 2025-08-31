# Leetcode 3002: Maximum Size of a Set After Removals
# https://leetcode.com/problems/maximum-size-of-a-set-after-removals/
# Solved on 31st of August, 2025
class Solution:
    def maximumSetSize(self, nums1: list[int], nums2: list[int]) -> int:
        """
        Calculates the maximum possible size of a set formed by taking at most n/2 elements from nums1 and at most n/2 elements from nums2.

        Args:
            nums1 (list[int]): The first list of integers.
            nums2 (list[int]): The second list of integers.

        Returns:
            int: The maximum possible size of the combined set.
        """
        n = len(nums1)
        half = n // 2
        s1 = set(nums1)
        s2 = set(nums2)
        only1 = len(s1 - s2)
        only2 = len(s2 - s1)
        common = len(s1 & s2)

        return min(n, common + min(only1, half) + min(only2, half))