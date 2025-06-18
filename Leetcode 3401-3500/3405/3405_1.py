# Leetcode 3405: Count the Number of Arrays with K Matching Adjacent Elements
# https://leetcode.com/problems/count-the-number-of-arrays-with-k-matching-adjacent-elements/
# Solved on 17th of June, 2025

class Solution:
    def countGoodArrays(self, n: int, m: int, k: int) -> int:
        """
        Counts the number of arrays of length n with elements from 1 to m
        such that there are exactly k pairs of adjacent equal elements.

        Args:
            n: The length of the array.
            m: The maximum value of elements in the array.
            k: The required number of adjacent equal pairs.

        Returns:
            The number of good arrays modulo 10^9 + 7.
        """
        modulus = 10**9 + 7

        if k > (n - 1):
            return 0

        preComputationLimit = n
        factorials = [1] * preComputationLimit
        inverseFactorials = [1] * preComputationLimit

        for i in range(1, preComputationLimit):
            factorials[i] = (factorials[i - 1] * i) % modulus

        inverseFactorials[preComputationLimit - 1] = pow(factorials[preComputationLimit - 1], modulus - 2, modulus)
        for i in range(preComputationLimit - 2, -1, -1):
            inverseFactorials[i] = (inverseFactorials[i + 1] * (i + 1)) % modulus

        def combinations(nVal, kVal):
            if kVal < 0 or kVal > nVal:
                return 0

            numerator = factorials[nVal]
            denominator = (inverseFactorials[kVal] * inverseFactorials[nVal - kVal]) % modulus
            return (numerator * denominator) % modulus

        combinationsCount = combinations(n - 1, k)

        powerOfMMinusOne = pow(m - 1, n - 1 - k, modulus)

        secondTerm = (m * powerOfMMinusOne) % modulus

        result = (combinationsCount * secondTerm) % modulus

        return result