# Leetcode 1520: Maximum Number of Non-Overlapping Substrings
# https://leetcode.com/problems/maximum-number-of-non-overlapping-substrings/
# Solved on 8th of July, 2025
class Solution:
    def maxNumOfSubstrings(self, s: str) -> list[str]:
        """
        Finds the maximum number of non-overlapping substrings such that each substring contains
        all occurrences of its constituent characters.

        Args:
            s: The input string.

        Returns:
            A list of non-overlapping substrings satisfying the conditions.
        """
        firstOccurrences = {}
        lastOccurrences = {}
        stringLength = len(s)

        for i, char in enumerate(s):
            if char not in firstOccurrences:
                firstOccurrences[char] = i
            lastOccurrences[char] = i

        validIntervals = []
        for i in range(stringLength):
            if i == firstOccurrences.get(s[i]):
                rightBoundary = lastOccurrences[s[i]]

                currentIndex = i
                isValid = True
                tempRightBoundary = rightBoundary

                while currentIndex <= tempRightBoundary:
                    if firstOccurrences[s[currentIndex]] < i:
                        isValid = False
                        break
                    tempRightBoundary = max(tempRightBoundary, lastOccurrences[s[currentIndex]])
                    currentIndex += 1

                if isValid:
                    validIntervals.append((i, tempRightBoundary))

        validIntervals.sort(key=lambda x: (x[1], x[1] - x[0]))

        result = []
        lastEnd = -1

        for left, right in validIntervals:
            if left > lastEnd:
                result.append(s[left:right + 1])
                lastEnd = right

        return result