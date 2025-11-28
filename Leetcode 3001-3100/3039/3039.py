# Leetcode 3039: Apply Operations to Make String Empty
# https://leetcode.com/problems/apply-operations-to-make-string-empty/
# Solved on 28th of November, 2025
class Solution:
    def lastNonEmptyString(self, s: str) -> str:
        """
        Given a string s, apply operations to make it empty.
        An operation consists of removing all occurrences of a character that appears at least once.
        Return the last non-empty string obtained.
        :param s: The input string.
        :return: The last non-empty string.
        """
        charCounts = {}
        for char in s:
            charCounts[char] = charCounts.get(char, 0) + 1

        maxFreq = 0
        for count in charCounts.values():
            if count > maxFreq:
                maxFreq = count

        resultChars = []
        seenChars = set()

        for i in range(len(s) - 1, -1, -1):
            currentChar = s[i]
            if charCounts[currentChar] == maxFreq:
                if currentChar not in seenChars:
                    resultChars.append(currentChar)
                    seenChars.add(currentChar)

        return "".join(resultChars[::-1])