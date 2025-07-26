# Leetcode 2179: Count Good Triplets in an Array
# https://leetcode.com/problems/count-good-triplets-in-an-array/

class FenwickTree:
    """
    A standard Fenwick Tree (Binary Indexed Tree) implementation.
    It supports point updates and prefix sum queries in O(log N) time.
    Uses 1-based indexing internally for tree structure convenience
    but accepts 0-based indices for external calls (add, query).
    """

    def __init__(self, size: int):
        self.tree = [0] * (size + 1)
        self._size = size

    def add(self, index: int, delta: int):
        i = index + 1

        while i <= self._size:
            self.tree[i] += delta
            i += i & (-i)

    def query(self, index: int) -> int:
        if index < 0:
            return 0
        i = index + 1
        s = 0

        while i > 0:
            s += self.tree[i]
            i -= i & (-i)

        return s


class Solution:
    def goodTriplets(self, nums1: list[int], nums2: list[int]) -> int:
        """
        Calculates the number of good triplets in the input lists nums1 and nums2. A triplet
        (i, j, k) is considered good if i < j < k and nums1[i], nums1[j], nums1[k] appear
        in the same order in nums2. This method employs Fenwick Trees to efficiently calculate
        the count of elements smaller to the left and larger to the right for optimizing the
        triplet search.

        :param nums1: The first input list of integers.
        :type nums1: list[int]
        :param nums2: The second input list of integers.
        :type nums2: list[int]
        :return: The count of good triplets present in nums1 and nums2.
        :rtype: int
        """
        n = len(nums1)
        if n < 3:
            return 0

        pos2_map = [0] * n
        for index, value in enumerate(nums2):
            pos2_map[value] = index

        A = [pos2_map[nums1[i]] for i in range(n)]

        smaller_left = [0] * n
        left_bit = FenwickTree(n)
        for j in range(n):
            val = A[j]
            smaller_left[j] = left_bit.query(val - 1)
            left_bit.add(val, 1)

        larger_right = [0] * n
        right_bit = FenwickTree(n)
        for j in range(n - 1, -1, -1):
            val = A[j]
            larger_right[j] = right_bit.query(n - 1) - right_bit.query(val)
            right_bit.add(val, 1)

        total_good_triplets = 0
        for i in range(1, n - 1):
            count_sm_left = smaller_left[j]
            count_lg_right = larger_right[j]
            count_lg_right = larger_right[j]

            if count_sm_left > 0 and count_lg_right > 0:
                total_good_triplets += count_sm_left * count_lg_right

        return total_good_triplets
