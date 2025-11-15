# Leetcode 1525: Number of Good Ways to Split a String
# https://leetcode.com/problems/number-of-good-ways-to-split-a-string/
# Solved on 15th of November, 2025
class Solution:
    def numSplits(self, s: str) -> int:
        """
        Calculates the number of "good" ways to split a string.
        A split is considered "good" if the number of distinct characters
        in the left substring is equal to the number of distinct characters
        in the right substring.

        Args:
            s (str): The input string.
        Returns:
            int: The number of good splits.
        """
        n = len(s)
        if n <= 1:
            return 0

        rightCounts = [0] * 26
        distinctRight = 0
        for char in s:
            index = ord(char) - ord('a')
            if rightCounts[index] == 0:
                distinctRight += 1
            rightCounts[index] += 1

        leftCounts = [0] * 26
        distinctLeft = 0
        goodSplits = 0

        for i in range(n - 1):
            char = s[i]
            leftIndex = ord(char) - ord('a')

            if leftCounts[leftIndex] == 0:
                distinctLeft += 1
            leftCounts[leftIndex] += 1

            rightIndex = leftIndex
            rightCounts[rightIndex] -= 1
            if rightCounts[rightIndex] == 0:
                distinctRight -= 1

            if distinctLeft == distinctRight:
                goodSplits += 1

        return goodSplits