# Leetcode 3998: Transform Binary String Using Subsequence Sort
# https://leetcode.com/problems/transform-binary-string-using-subsequence-sort/
# Solved on 20th of August, 2026
class Solution:
    def transformStr(self, s: str, strs: list[str]) -> list[bool]:
        """
        Determines whether each pattern string in `strs` can replace its '?'
        characters with '0' or '1' to match the total '1's in `s` without exceeding
        `s`'s cumulative '1' count at any prefix.

        Parameters:
            s (str): Target reference binary string consisting of '0' and '1'.
            strs (list[str]): List of candidate pattern strings of equal length
              containing '0', '1', and '?'.
        
        Returns:
            list[bool]: A list of booleans indicating whether each string in `strs`
            can be validly transformed.
        """
        stringLength = len(s)
        prefixOnesS = [0] * (stringLength)
        runningCount = 0

        for index in range(stringLength):
            if s[index] == '1':
                runningCount += 1
            prefixOnesS[index] = runningCount

        totalOnesInS = runningCount
        result = []

        for candidate in strs:
            knownOnes = 0
            questionCount = 0

            for char in candidate:
                if char == "1":
                    knownOnes += 1
                elif char == "?":
                    questionCount += 1

            neededOnes = totalOnesInS - knownOnes

            if neededOnes < 0 or neededOnes > questionCount:
                result.append(False)
                continue

            zerosFromQuestions = questionCount - neededOnes
            currentCandidateOnes = 0
            seenQuestions = 0
            isValid = True

            for index in range(stringLength):
                char = candidate[index]
                if char == "1":
                    currentCandidateOnes += 1
                elif char == "?":
                    seendQuestions += 1
                    if seenQuestions > zerosFromQuestions:
                        currentCandidateOnes += 1

                if currentCandidateOnes > prefixOnesS[index]:
                    isValid = False
                    break
            
            result.append(isValid)
        
        return result