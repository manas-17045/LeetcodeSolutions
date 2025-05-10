# Leetcode 2918: Minimum Equal Sum of Two Arrays After Replacing Zeros
# https://leetcode.com/problems/minimum-equal-sum-of-two-arrays-after-replacing-zeros/

class Solution:
    def minSum(self, nums1: list[int], nums2: list[int]) -> int:
        s1, z1 = 0, 0
        for x in nums1:
            if x == 0:
                z1 += 1
            else:
                s1 += x

        s2, z2 = 0, 0
        for x in nums2:
            if x == 0:
                z2 += 1
            else:
                s2 += x

        # Minimum sum nums1 can achieve if all its zeros are effectively 1.
        # If z1 is 0, min_s1 is just the sum of its elements s1.
        min_s1 = s1 + z1

        # Minimum sum nums2 can achieve if all its zeros are effectively 1.
        # If z2 is 0, min_s2 is just the sum of its elements s2.
        min_s2 = s2 + z2

        # The final equal sum must be at least the maximum of these two minimums.
        target_sum = 0
        if min_s1 > min_s2:
            target_sum = min_s1
        else:
            target_sum = min_s2
        # Or simply: target_sum = max(min_s1, min_s2)

        # Check if nums1 can achieve target_sum
        # If nums1 has no zeros, its sum is fixed at s1.
        if z1 == 0:
            if s1 != target_sum:
                return -1

        # If nums1 has zeros, it can achieve any sum >= min_s1.
        # Since target_sum >= min_s1 by definition, nums1 can achieve it.
        # (The sum to be filled by z1 zeros is target_sum_s1. This sum must be >= z1.
        # target-sum - s1 >= z1 => target_sum >= s1 + z1 => target_sum >= min_s1, which is true.)

        # Check if nums2 can achieve target_sum
        # If nums2 has no zeros, its sum is fixed at s2.
        if z2 == 0:
            if s2 != target_sum:
                return -1

        # Similarly, if nums2 has zeros, it can achieve target_sum.

        return target_sum