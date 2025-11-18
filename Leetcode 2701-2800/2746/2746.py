# Leetcode 2746: Decremental String Concatenation
# https://leetcode.com/problems/decremental-string-concatenation/
# Solved on 18th of November, 2025
class Solution:
    def minimizeConcatenatedLength(self, words: list[str]) -> int:
        """
        Minimizes the total length of a concatenated string formed by a given list of words.
        When concatenating two words, if the last character of the first word is the same
        as the first character of the second word, one character is "saved" (i.e., the
        overlapping character is counted only once).

        :param words: A list of strings to be concatenated.
        :return: The minimum possible length of the concatenated string.
        """
        dp = {(words[0][0], words[0][-1]): len(words[0])}

        for i in range(1, len(words)):
            currentWord = words[i]
            currentLen = len(currentWord)
            startChar = currentWord[0]
            endChar = currentWord[-1]
            nextDp = {}

            for (prevStart, prevEnd), prevLen in dp.items():
                len1 = prevLen + currentLen - (1 if prevEnd == startChar else 0)
                state1 = (prevStart, endChar)
                if state1 not in nextDp or len1 < nextDp[state1]:
                    nextDp[state1] = len1

                len2 = prevLen + currentLen - (1 if endChar == prevStart else 0)
                state2 = (startChar, prevEnd)
                if state2 not in nextDp or len2 < nextDp[state2]:
                    nextDp[state2] = len2

            dp = nextDp

        return min(dp.values())