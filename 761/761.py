# Leetcode 761: Special Binary String
# https://leetcode.com/problems/special-binary-string/
# Solved on 20th of February, 2026
class Solution:
    def makeLargestSpecial(self, s: str) -> str:
        """
        Rearranges the special binary string to make it lexicographically largest.

        :param s: A special binary string.
        :return: The lexicographically largest special binary string after any number of swaps.
        """
        balanceCount = 0
        startIndex = 0

        validSubstrings = []
        for endIndex, currentChar in enumerate(s):
            balanceCount += 1 if currentChar == '1' else -1

            if balanceCount == 0:
                innerString = self.makeLargestSpecial(s[startIndex + 1:endIndex])
                validSubstrings.append('1' + innerString + '0')
                startIndex = endIndex + 1

        validSubstrings.sort(reverse=True)

        return "".join(validSubstrings)