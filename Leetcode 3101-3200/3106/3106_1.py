# Leetcode 3106: Lexicographically Smallest String After Operations With Constraint
# https://leetcode.com/problems/lexicographically-smallest-string-after-operations-with-constraint/
# Solved on 18th of June, 2025

class Solution:
    def getSmallestString(self, s: str, k: int) -> str:
        """
        Given a string s and an integer k, return the lexicographically smallest string
        that can be obtained after performing at most k operations.
        In one operation, you can change any character of the string to the previous
        lowercase English letter, with 'a' wrapping around to 'z', or the next
        lowercase English letter, with 'z' wrapping around to 'a'.

        :param s: The input string.
        :param k: The maximum number of operations allowed.
        """
        resultChars = []
        remainingK = k

        for currentChar in s:
            if remainingK == 0:
                resultChars.append(currentChar)
                continue

            charValue = ord(currentChar) - ord('a')
            distanceToA = min(charValue, (26 - charValue))

            if remainingK >= distanceToA:
                resultChars.append('a')
                remainingK -= distanceToA
            else:
                newChar = chr(ord(currentChar) - remainingK)
                resultChars.append(newChar)
                remainingK = 0

        return "".join(resultChars)