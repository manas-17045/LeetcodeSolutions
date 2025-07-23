# Leetcode 1638: Count Substrings That Differ by One Character
# https://leetcode.com/problems/count-substrings-that-differ-by-one-character/
# Solved on 23rd of July, 2025
class Solution:
    def countSubstrings(self, s: str, t: str) -> int:
        """
        Counts the number of pairs of non-empty substrings (sub_s, sub_t) such that sub_s is a substring of s,
        sub_t is a substring of t, sub_s and sub_t have the same length, and they differ by exactly one character.

        :param s: The first input string.
        :param t: The second input string.
        :return: The total count of such substring pairs.
        """
        lenS = len(s)
        lenT = len(t)

        totalCount = 0

        prevDp0 = [0] * (lenT + 1)
        prevDp1 = [0] * (lenT + 1)

        for i in range(1, (lenS + 1)):
            currDp0 = [0] * (lenT + 1)
            currDp1 = [0] * (lenT + 1)
            for j in range(1, (lenT + 1)):
                if s[i - 1] == t[j - 1]:
                    currDp0[j] = 1 +prevDp0[j - 1]
                    currDp1[j] = prevDp1[j - 1]
                else:
                    currDp1[j] = 1 + prevDp0[j - 1]

                totalCount += currDp1[j]

            prevDp0 = currDp0
            prevDp1 = currDp1

        return totalCount