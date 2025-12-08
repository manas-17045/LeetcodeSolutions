# Leetcode 3233: Find the Count of Numbers Which Are Not Special
# https://leetcode.com/problems/find-the-count-of-numbers-which-are-not-special/
# Solved on 8th of December, 2025
class Solution:
    def nonSpecialCount(self, l: int, r: int) -> int:
        """
        Calculates the count of numbers in the range [l, r] that are not "special".
        A number is considered "special" if it is the square of a prime number.
        :param l: The lower bound of the range (inclusive).
        :param r: The upper bound of the range (inclusive).
        :return: The count of non-special numbers in the given range.
        """
        upperLimit = int(r ** 0.5)
        isPrime = [True] * (upperLimit + 1)
        isPrime[0] = isPrime[1] = False
        for i in range(2, int(upperLimit ** 0.5) + 1):
            if isPrime[i]:
                for j in range(i * i, upperLimit + 1, i):
                    isPrime[j] = False

        specialCount = 0
        for i in range(2, upperLimit + 1):
            if isPrime[i]:
                squaredVal = i * i
                if squaredVal >= l:
                    specialCount += 1

        totalNums = r - l + 1
        return totalNums - specialCount