# Leetcode 2040: Kth Smallest Product of Two Sorted Arrays
# https://leetcode.com/problems/kth-smallest-product-of-two-sorted-arrays/
# Solved on 25th of June, 2025
import bisect


class Solution:
    def kthSmallestProduct(self, nums1: list[int], nums2: list[int], k: int) -> int:
        """
        Finds the k-th smallest product of two numbers, one from nums1 and one from nums2.

        Args:
            nums1: A list of integers, sorted in non-decreasing order.
            nums2: A list of integers, sorted in non-decreasing order.
            k: The k-th smallest product to find.

        Returns:
            The k-th smallest product.
        """
        n2Len = len(nums2)

        def countLessEqual(val: float) -> int:
            currentCount = 0
            for x in nums1:
                if x > 0:
                    target = val / x
                    idx = bisect.bisect_right(nums2, target)
                    currentCount += idx
                elif x < 0:
                    target = val / x
                    idx = bisect.bisect_left(nums2, target)
                    currentCount += (n2Len - idx)
                else:
                    if val >= 0:
                        currentCount += n2Len
            return currentCount

        low = -10**10
        high = 10**10

        finalAns = high

        while low <= high:
            mid = low + (high - low) // 2

            if countLessEqual(float(mid)) >= k:
                finalAns = mid
                high = mid - 1
            else:
                low = mid + 1

        return finalAns