# Leetcode 2546: Apply Bitwise Operations to Make Strings Equal
# https://leetcode.com/problems/apply-bitwise-operations-to-make-strings-equal/
# Solved on 17th of July, 2025
class Solution:
    def makeStringsEqual(self, s: str, target: str) -> bool:
        """
        Determines if string `s` can be transformed into string `target` using bitwise operations.

        :param s: The source binary string.
        :param target: The target binary string.
        :return: True if `s` can be transformed into `target`, False otherwise.
        """
        sHasOne = '1' in s
        targetHasOne = '1' in target
        return sHasOne == targetHasOne