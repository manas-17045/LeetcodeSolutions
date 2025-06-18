# Leetcode 3981: Replace Question Marks in String to Minimize Its Value
# https://leetcode.com/problems/replace-question-marks-in-string-to-minimize-its-value/
# Solved on 18th of June, 2025
import heapq
from collections import Counter


class Solution:
    def minimizeStringValue(self, s: str) -> str:
        """
        Replaces question marks in a string with lowercase letters to minimize the string's value.
        The value of a string is the sum of the values of its characters, where the value of a
        character is its frequency in the string.

        Args:
            s: The input string containing lowercase letters and '?'.
        Returns:
            The string with '?' replaced to minimize the total value.
        """
        initialCharCounts = Counter()
        questionMarkIndices = []

        for i, charInS in enumerate(s):
            if charInS == '?':
                questionMarkIndices.append(i)
            else:
                initialCharCounts[charInS] += 1

        minHeap = []
        for i in range(26):
            charValue = chr(ord('a') + i)
            heapq.heappush(minHeap, (initialCharCounts[charValue], charValue))

        numQuestionMarks = len(questionMarkIndices)
        charsToUseForReplacement = []

        for _ in range(numQuestionMarks):
            currentCount, charValueToUse = heapq.heappop(minHeap)
            charsToUseForReplacement.append(charValueToUse)
            heapq.heappush(minHeap, (currentCount + 1, charValueToUse))

        charsToUseForReplacement.sort()

        resultCharsList = list(s)
        for i in range(numQuestionMarks):
            originalIndex = questionMarkIndices[i]
            replacementChar = charsToUseForReplacement[i]
            resultCharsList[originalIndex] = replacementChar

        return "".join(resultCharsList)