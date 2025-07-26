# Leetcode 2179: Count Good Triplets in an Array
# https://leetcode.com/problems/count-good-triplets-in-an-array/
# Solved on 26th of July, 2025
class Solution:
    def goodTriplets(self, nums1: list[int], nums2: list[int]) -> int:
        """
        Counts the number of good triplets (i, j, k) such that nums1[i] < nums1[j] < nums1[k]
        and their corresponding indices in nums2 also satisfy nums2_idx[i] < nums2_idx[j] < nums2_idx[k].
        :param nums1: A list of integers representing the first permutation.
        :param nums2: A list of integers representing the second permutation.
        :return: The total count of good triplets.
        """
        class FenwickTree:
            def __init__(self, size):
                self.tree = [0] * (size + 1)

            def update(self, index, delta):
                while index < len(self.tree):
                    self.tree[index] += delta
                    index += index & (-index)

            def query(self, index):
                s = 0
                while index > 0:
                    s += self.tree[index]
                    index -= index & (-index)
                return s

        n = len(nums1)
        posMap = {val: i for i, val in enumerate(nums2)}

        bit = FenwickTree(n)
        result = 0

        for i in range(n):
            val = nums1[i]
            pos2 = posMap[val]

            leftCount = bit.query(pos2)

            rightCount = (n - 1 - pos2) - (i - leftCount)

            result += leftCount * rightCount

            bit.update(pos2 + 1, 1)

        return result