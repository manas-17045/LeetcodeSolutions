# Leetcode 2569: Handling Sum Queries After Update
# https://leetcode.com/problems/handling-sum-queries-after-update/
# Solved on 4th of December, 2025
class Solution:
    def handleQuery(self, nums1: list[int], nums2: list[int], queries: list[list[int]]) -> list[int]:
        """
        Handles sum queries after updates on two arrays.

        Args:
            nums1: A list of integers representing the first array (binary).
            nums2: A list of integers representing the second array.
            queries: A list of queries, where each query is a list of integers.

        Returns:
            A list of integers representing the results of type 3 queries.
        """

        sumNums2 = sum(nums2)
        nums1Val = int("".join(map(str, nums1[::-1])), 2)
        result = []

        for op, l, r in queries:
            if op == 1:
                mask = ((1 << (r - l + 1)) - 1) << l
                nums1Val ^= mask
            elif op == 2:
                sumNums2 += l * nums1Val.bit_count()
            else:
                result.append(sumNums2)

        return result