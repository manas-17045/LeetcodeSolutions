# Leetcode 3598: Longest Common Prefix Between Adjacent Strings After Removals
# https://leetcode.com/problems/longest-common-prefix-between-adjacent-strings-after-removals/
# Solved on 13th of September, 2025
class Solution:
    def longestCommonPrefix(self, words: list[str]) -> list[int]:
        """
        Calculates the longest common prefix (LCP) between adjacent strings after removing one string.

        Args:
            words: A list of strings.
        Returns:
            A list of integers, where each element at index `i` represents the maximum LCP possible
            between any two adjacent strings in the remaining sequence after removing `words[i]`.
        """
        numWords = len(words)

        if numWords <= 1:
            return [0] * numWords

        def getLCPLength(strOne: str, strTwo: str) -> int:
            commonLength = 0
            for charOne, charTwo in zip(strOne, strTwo):
                if charOne == charTwo:
                    commonLength += 1
                else:
                    break
            return commonLength

        lcpValues = [0] * (numWords - 1)
        for i in range(numWords - 1):
            lcpValues[i] = getLCPLength(words[i], words[i + 1])

        prefixMax = [0] * (numWords - 1)
        prefixMax[0] = lcpValues[0]
        for i in range(1, numWords - 1):
            prefixMax[i] = max(prefixMax[i - 1], lcpValues[i])

        suffixMax = [0] * (numWords - 1)
        suffixMax[numWords - 2] = lcpValues[numWords - 2]
        for i in range(numWords - 3, -1, -1):
            suffixMax[i] = max(suffixMax[i + 1], lcpValues[i])

        answer = [0] * numWords
        for i in range(numWords):
            currentMaxLcp = 0

            if i >= 2:
                currentMaxLcp = max(currentMaxLcp, prefixMax[i - 2])

            if i < numWords - 2:
                currentMaxLcp = max(currentMaxLcp, suffixMax[i + 1])

            if i > 0 and i < (numWords - 1):
                newLcp = getLCPLength(words[i - 1], words[i + 1])
                currentMaxLcp = max(currentMaxLcp, newLcp)

            answer[i] = currentMaxLcp

        return answer