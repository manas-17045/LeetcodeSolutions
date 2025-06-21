# Leetcode 1835: Find XOR Sum of All pairs Bitwise AND
# https://leetcode.com/problems/find-xor-sum-of-all-pairs-bitwise-and/
# Solved on 21st of June, 2025
class Solution:
    def getXORSum(self, arr1: list[int], arr2: list[int]) -> int:
        """
        Calculates the XOR sum of all pairs (a, b) where a is from arr1 and b is from arr2,
        and the operation is (a AND b).

        This is based on the property: (A XOR B) AND (C XOR D) = (A AND C) XOR (A AND D) XOR (B AND C) XOR (B AND D)
        More generally, (XOR_sum(arr1)) AND (XOR_sum(arr2)) = XOR_sum(a AND b for all a in arr1, b in arr2)
        """
        xorSumArr1 = 0
        for num in arr1:
            xorSumArr1 ^= num

        xorSumArr2 = 0
        for num in arr2:
            xorSumArr2 ^= num

        return xorSumArr1 & xorSumArr2