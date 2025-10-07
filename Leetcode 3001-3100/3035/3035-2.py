# Leetcode 3035: Maximum Palindromes After Operations
# https://leetcode.com/problems/maximum-palindromes-after-operations/
# Solved on 7th of October, 2025
from collections import Counter


class Solution:
    def maxPalindromesAfterOperations(self, words: list[str]) -> int:
        """
        Calculates the maximum number of palindromes that can be formed from a given list of words
        by rearranging their characters.

        :param words: A list of strings.
        :return: The maximum number of palindromes that can be formed.
        """
        # Count frequency of all characters across all words
        char_count = Counter()
        for word in words:
            char_count.update(word)

        # Calculate total number of character pairs available
        total_pairs = sum(count // 2 for count in char_count.values())

        # Sort words by length (greedy: form shortest palindromes first)
        word_lengths = sorted(len(word) for word in words)

        # Try to form palindromes starting with shortest words
        palindromes = 0
        for length in word_lengths:
            # Pairs needed for this word
            pairs_needed = length // 2

            if total_pairs >= pairs_needed:
                # We can form a palindrome for this word
                total_pairs -= pairs_needed
                palindromes += 1
            else:
                # Not enough pairs left
                break

        return palindromes