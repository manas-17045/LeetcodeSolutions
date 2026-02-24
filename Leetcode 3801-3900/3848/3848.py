# Leetcode 3848: Check Digitorial Permutation
# https://leetcode.com/problems/check-digitorial-permutation/
# Solved on 24th of February, 2026
class Solution:
    def isDigitorialPermutation(self, n: int) -> bool:
        """
        Checks if the given integer n is a digitorial permutation.

        :param n: The integer to check.
        :return: True if n is a digitorial permutation, False otherwise.
        """
        sortedStr = "".join(sorted(str(n)))
        return sortedStr in ("1", "2", "145", "04558")