# Leetcode 2472: Maximum Number of Non-overlapping Palindrome Substrings
# https://leetcode.com/problems/maximum-number-of-non-overlapping-palindrome-substrings/
# Solved on 7th of July, 2025
class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        """
        Given a string `s` and an integer `k`, return the maximum number of non-overlapping palindrome substrings of `s` such that the length of each palindrome substring is at least `k`.

        A substring is a contiguous non-empty sequence of characters within a string.

        Args:
            s (str): The input string.
            k (int): The minimum length required for a palindrome substring.

        Returns:
            int: The maximum number of non-overlapping palindrome substrings.
        """
        stringLength = len(s)
        minLength = k

        isPalindrome = [[False] * stringLength for _ in range(stringLength)]

        for i in range((stringLength - 1), -1, -1):
            for j in range(i, stringLength):
                if s[i] == s[j]:
                    if (j - i) < 2:
                        isPalindrome[i][j] = True
                    else:
                        isPalindrome[i][j] = isPalindrome[i + 1][j - 1]

        memo = {}

        def findMax(startIndex):
            if startIndex >= stringLength:
                return 0

            if startIndex in memo:
                return memo[startIndex]

            count = findMax(startIndex + 1)

            for endIndex in range((startIndex + minLength - 1), stringLength):
                if isPalindrome[startIndex][endIndex]:
                    count = max(count, (1 + findMax(endIndex + 1)))

            memo[startIndex] = count
            return count

        return findMax(0)