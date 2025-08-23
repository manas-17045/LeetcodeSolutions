# Leetcode 2657: Find the Prefix Common Array of Two Arrays
# https://leetcode.com/problems/find-the-prefix-common-array-of-two-arrays/
# Solved on 23rd of August, 2025
class Solution:
    def findThePrefixCommonArray(self, A: list[int], B: list[int]) -> list[int]:
        """
        Calculates the common elements in prefixes of two arrays.

        Args:
            A (list[int]): The first input array.
            B (list[int]): The second input array.
        Returns:
            list[int]: A list where res[i] is the number of common elements in A[0...i] and B[0...i].
        """
        n = len(A)
        counts = bytearray(n + 1)  # counts[x] will be 0,1,or 2
        common = 0
        res = [0] * n

        for i in range(n):
            a = A[i]
            counts[a] += 1
            if counts[a] == 2:
                common += 1

            b = B[i]
            counts[b] += 1
            if counts[b] == 2:
                common += 1

            res[i] = common

        return res