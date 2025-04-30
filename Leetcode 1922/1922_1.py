# Leetcode 1922: Count Good Numbers
# https://leetcode.com/problems/count-good-numbers/

class Solution:
    def countGoodNumbers(self, n: int) -> int:
        """
        Calculate the number of valid "good numbers" based on the given rules for placement
        of even digits and prime digits for a number of a given length. A "good number" is
        defined such that:
        - Even indices can only contain even digits (0, 2, 4, 6, 8).
        - Odd indices can only contain prime digits (2, 3, 5, 7).

        The computation is performed modulo 10^9 + 7 to avoid overflow for large values of `n`.

        :param n: The length of the number to be checked.
        :type n: int

        :return: The count of valid "good numbers" is modulo 10^9 + 7.
        :rtype: int
        """
        MOD = 10 ** 9 + 7

        num_even_indices = (n + 1) // 2
        num_odd_indices = n // 2

        count_even_choices = pow(5, num_even_indices, MOD)
        count_odd_choices = pow(4, num_odd_indices, MOD)

        total_count = (count_even_choices * count_odd_choices) % MOD

        return total_count