# Leetcode 2310: Sum of Numbers With Units Digit K
# https://leetcode.com/problems/sum-of-numbers-with-units-digit-k/
# Solved on 17th of September, 2025
class Solution:
    def minimumNumbers(self, num: int, k: int) -> int:
        """
        Finds the minimum size of a set of positive integers, where each integer
        in the set has a units digit of k, and the sum of the integers in the set
        equals `num`.

        Args:
            num (int): The target sum.
            k (int): The required units digit for each number in the set.

        Returns:
            int: The minimum size of such a set. Returns -1 if no such set exists.
                 Returns 0 if num is 0.
        """
        if num == 0:
            return 0

        for sizeOfSet in range(1, 11):
            product = sizeOfSet * k
            if product <= num and product % 10 == num % 10:
                return sizeOfSet

        return -1