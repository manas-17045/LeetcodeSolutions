# Leetcode 2310: Sum of Numbers With Units Digit K
# https://leetcode.com/problems/sum-of-numbers-with-units-digit-k/
# Solved on 17th of September, 2025
class Solution:
    def minimumNumbers(self, num: int, k: int) -> int:
        """
        Finds the minimum number of positive integers, each ending with digit k, that sum up to num.
        :param num: The target sum.
        :param k: The required last digit of the integers.
        :return: The minimum count of such numbers, or -1 if no such combination exists.
        """
        # Sum 0 -> empty set
        if num == 0:
            return 0

        # If num ends with 0, num itself is a valid single number
        if k == 0:
            return 1 if num % 10 == 0 else -1

        # Try using i numbers from 1 to 10
        for i in range(1, 11):
            s = i * k
            if s <= num and (num - s) % 10 == 0:
                return i

        return -1