# Leetcode 3002: Maximum Size of a Set After Removals
# https://leetcode.com/problems/maximum-size-of-a-set-after-removals/
# Solved on 31st of August, 2025
class Solution:
    def maximumSetSize(self, nums1: list[int], nums2: list[int]) -> int:
        """
        Calculates the maximum possible size of a set formed by taking n/2 elements from nums1
        and n/2 elements from nums2, such that the combined set has the maximum number of unique elements.

        Args:
            nums1 (list[int]): The first list of integers.
            nums2 (list[int]): The second list of integers.

        Returns:
            int: The maximum size of the combined set.
        """

        n = len(nums1)
        halfN = n // 2

        s1 = set(nums1)
        s2 = set(nums2)

        unique1 = s1 - s2
        unique2 = s2 - s1
        common = s1 & s2

        # Greedily keep elements that are unique to s1.
        canKeepUnique1 = min(len(unique1), halfN)

        # Greedily keep elements that are unique to s2.
        canKeepUnique2 = min(len(unique2), halfN)

        # Calculate remaining slots for each array to keep common elements.
        remainingSlots1 = halfN - canKeepUnique1
        remainingSlots2 = halfN - canKeepUnique2

        # The number of common elements we can add to the final set is limited
        # by the number available and the total remaining slots from both arrays.
        canKeepCommon = min(len(common), remainingSlots1 + remainingSlots2)

        # The total size is the sum of all distinct elements kept.
        return canKeepUnique1 + canKeepUnique2 + canKeepCommon