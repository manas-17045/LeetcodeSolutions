# Leetcode 696: Count Binary Substrings
# https://leetcode.com/problems/count-binary-substrings/
# Solved on 19th of February, 2026
class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        """
        Counts the number of non-empty substrings that have the same number of 0's and 1's,
        and all the 0's and all the 1's in these substrings are grouped consecutively.

        :param s: A binary string.
        :return: The number of valid binary substrings.
        """
        totalCount = 0
        prevLength = 0
        currLength = 1
        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                currLength += 1
            else:
                totalCount += min(prevLength, currLength)
                prevLength = currLength
                currLength = 1

        totalCount += min(prevLength, currLength)
        return totalCount