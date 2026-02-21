# Leetcode 762: Prime Number of Set Bits in Binary Representation
# https://leetcode.com/problems/prime-number-of-set-bits-in-binary-representation/
# Solved on 21st of February, 2026
class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        """
        Counts the number of integers in the range [left, right] that have a prime number of set bits.

        :param left: The starting integer of the range.
        :param right: The ending integer of the range.
        :return: The total count of numbers with a prime number of set bits.
        """
        primeSet = {2, 3, 5, 7, 11, 13, 17, 19}
        validCount = 0
        for currentNumber in range(left, right + 1):
            if currentNumber.bit_count() in primeSet:
                validCount += 1

        return validCount