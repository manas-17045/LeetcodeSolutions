# Leetcode 2918: Minimum Equal Sum of Two Arrays After Replacing Zeros
# https://leetcode.com/problems/minimum-equal-sum-of-two-arrays-after-replacing-zeros/

class Solution:
    def minSum(self, nums1: list[int], nums2: list[int]) -> int:
        """
        Calculates the minimum possible value of the maximum sum between two lists, considering
        their respective sums and the counts of zeros within each list. The function evaluates
        whether adding zeros from one list to the other's sum can result in balancing the sums
        or achieving a feasible maximum sum. If not, it returns -1 as a failure case.

        :param nums1: First list of integers.
        :param nums2: Second list of integers.
        :return: An integer representing the maximum sum considering the zeros in the lists,
            or -1 if conditions are not satisfied.
        """
        sum1 = sum(nums1)
        sum2 = sum(nums2)
        z1 = nums1.count(0)
        z2 = nums2.count(0)

        if z1 == 0 and sum1 < sum2 + z2:
            return -1
        if z2 == 0 and sum2 < sum1 + z1:
            return -1

        return max(sum1 + z1, sum2 + z2)