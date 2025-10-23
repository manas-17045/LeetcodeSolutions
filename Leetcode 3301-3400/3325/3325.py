# Leetcode 3325: Count Substrings With K-Frequency Characters I
# https://leetcode.com/problems/count-substrings-with-k-frequency-characters-i/
# Solved on 23rd of October, 2025
class Solution:
    def numberOfSubstrings(self, s: str, k: int) -> int:
        """
        Counts the number of substrings where each character appears at least k times.

        Args:
            s (str): The input string.
            k (int): The minimum frequency required for each character in a valid substring.

        Returns:
            int: The number of substrings where each character appears at least k times.
        """
        strLen = len(s)
        totalCount = strLen * (strLen + 1) // 2
        invalidCount = 0
        charCounts = [0] * 26
        leftPtr = 0

        for rightPtr in range(strLen):
            rightCharIdx = ord(s[rightPtr]) - ord('a')
            charCounts[rightCharIdx] += 1

            while charCounts[rightCharIdx] >= k:
                leftCharIdx = ord(s[leftPtr]) - ord('a')
                charCounts[leftCharIdx] -= 1
                leftPtr += 1

            invalidCount += (rightPtr - leftPtr + 1)

        return totalCount - invalidCount