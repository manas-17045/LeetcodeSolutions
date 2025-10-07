# Leetcode 3035: Maximum Palindromes After Operations
# https://leetcode.com/problems/maximum-palindromes-after-operations/
# Solved on 7th of October, 2025
import collections


class Solution:
    def maxPalindromesAfterOperations(self, words: list[str]) -> int:
        """
        Calculates the maximum number of palindromes that can be formed from the given words
        after operations.
        :param words: A list of strings.
        :return: The maximum number of palindromes.
        """
        # Count all characters and determine the total number of pairs
        charCounts = collections.Counter("".join(words))
        totalPairs = sum(count // 2 for count in charCounts.values())

        # Get a list of word lengths and sort it in ascending order
        wordLengths = sorted(len(word) for word in words)

        # Greedily form l=palindromes for the shortest words first
        palindromesCount = 0
        for length in wordLengths:
            # A word of length 'length' needs 'length // 2' pairs to be a palindrome
            pairsNeeded = length // 2

            if totalPairs >= pairsNeeded:
                # If we have enough pairs, use them and count this word.
                totalPairs -= pairsNeeded
                palindromesCount += 1
            else:
                break

        return palindromesCount