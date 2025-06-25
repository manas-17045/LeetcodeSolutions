# Leetcode 2040: Kth Smallest Product of Two Sorted Arrays
# https://leetcode.com/problems/kth-smallest-product-of-two-sorted-arrays/
# Solved on 25th of June, 2025
import bisect


class Solution:
    def kthSmallestProduct(self, nums1: list[int], nums2: list[int], k: int) -> int:
        """
        Finds the k-th smallest product among all possible products of elements from nums1 and nums2.

        The approach uses binary search on the answer (the k-th smallest product).
        For a given `mid` value, it counts how many products are less than or equal to `mid`.
        This count is then used to adjust the binary search range.

        Args:
            nums1: A list of integers.
            nums2: A list of integers.
            k: The k-th smallest product to find.

        Returns:
            The k-th smallest product.
        """
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        def count_leq(mid: int) -> int:
            cnt = 0
            n2 = len(nums2)
            for x in nums1:
                if x == 0:
                    if mid >= 0:
                        cnt += n2
                elif x > 0:
                    t = mid // x
                    cnt += bisect.bisect_right(nums2, t)
                else:
                    q, r = divmod(mid, x)
                    t = q if r == 0 else (q + 1)
                    cnt += n2 - bisect.bisect_left(nums2, t)
            return cnt

        low, high = -10**10-1, 10**10+1
        while low < high:
            mid = (low + high) // 2
            if count_leq(mid) >= k:
                high = mid
            else:
                low = mid + 1
        return low