# Leetcode 3855: Sum of K-Digit Numbers in a Range
# https://leetcode.com/problems/sum-of-k-digit-numbers-in-a-range/
# Solved on 1st of March, 2026
class Solution:
    def sumOfNumbers(self, l: int, r: int, k: int) -> int:
        """
        Calculates the sum of all k-digit numbers where each digit is in the range [l, r].

        :param l: The lower bound of the allowed digits (inclusive).
        :param r: The upper bound of the allowed digits (inclusive).
        :param k: The number of digits in each number.
        :return: The total sum of all valid k-digit numbers modulo 10^9 + 7.
        """
        modVal = 1000000007

        numChoices = r - l + 1
        sumDigits = (l + r) * numChoices // 2
        invNine = pow(9, modVal - 2, modVal)
        powTen = pow(10, k, modVal)
        repOnes = (powTen - 1) * invNine % modVal
        powChoices = pow(numChoices, k - 1, modVal)
        totalSum = (sumDigits * powChoices % modVal) * repOnes % modVal

        return totalSum