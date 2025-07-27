# Leetcode 1537: Get the Maximum Score
# https://leetcode.com/problems/get-the-maximum-score/
# Solved on 27th of July, 2025
class Solution:
    def maxSum(self, nums1: list[int], nums2: list[int]) -> int:
        """
        Calculates the maximum path sum from the start of two sorted arrays,
        allowing switching between arrays only at common elements.

        Args:
            nums1 (list[int]): The first sorted array of unique positive integers.
            nums2 (list[int]): The second sorted array of unique positive integers.
        Returns:
            int: The maximum path sum modulo 10^9 + 7.
        """
        MOD = 10 ** 9 + 7
        i, j = 0, 0
        sum1, sum2 = 0, 0
        n1, n2 = len(nums1), len(nums2)

        # Traverse both arrays
        while i < n1 and j < n2:
            if nums1[i] < nums2[j]:
                sum1 += nums1[i]
                i += 1
            elif nums1[i] > nums2[j]:
                sum2 += nums2[j]
                j += 1
            else:
                # Common element: take max path so far + this element
                common = nums1[i]
                best = max(sum1, sum2) + common
                sum1 = sum2 = best
                i += 1
                j += 1

        # Add remaining tail from nums1
        while i < n1:
            sum1 += nums1[i]
            i += 1

        # Add remaining tail from nums2
        while j < n2:
            sum2 += nums2[j]
            j += 1

        # The result is the max of the two possible sums, modded
        return max(sum1, sum2) % MOD