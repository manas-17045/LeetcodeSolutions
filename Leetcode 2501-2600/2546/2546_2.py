# Leetcode 2546: Apply Bitwise Operations to Make Strings Equal
# https://leetcode.com/problems/apply-bitwise-operations-to-make-strings-equal/
# Solved on 17th of July, 2025
class Solution:
    def makeStringsEqual(self, s: str, target: str) -> bool:
        """
        Determines if two binary strings can be made equal by repeatedly applying an operation.

        :param s: The first binary string.
        :param target: The second binary string.
        :return: True if the strings can be made equal, False otherwise.
        """
        return ('1' in s) == ('1' in target)