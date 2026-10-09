# Leetcode 1541: Minimum Insertions to Balance a Parentheses String
# https://leetcode.com/problems/minimum-insertions-to-balance-a-parentheses-string/
# Solved on 9th of October, 2026
class Solution:
    def minInsertions(self, s: str) -> int:
        """
        Calculates the minimum number of insertions required to balance a parentheses string.

        Parameters:
            s (str): The input string containing '(' and ')' characters.

        Returns:
            int: The minimum number of insertions needed to make the string balanced.
        """
        insertionsNeeded = 0
        openCount = 0
        currentIndex = 0
        stringLength = len(s)

        while currentIndex < stringLength:
            if s[currentIndex] == '(':
                openCount += 1
                currentIndex += 1
            else:
                if currentIndex + 1 < stringLength and s[currentIndex + 1] == ')':
                    currentIndex += 2
                else:
                    insertionsNeeded += 1
                    currentIndex += 1

                if openCount > 0:
                    openCount -= 1
                else:
                    insertionsNeeded += 1

        insertionsNeeded += openCount * 2
        return insertionsNeeded