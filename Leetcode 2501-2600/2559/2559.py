# Leetcode 2559: Count Vowel Strings in Ranges
# https://leetcode.com/problems/count-vowel-strings-in-ranges/
# Solved on 30th of November, 2025
class Solution:
    def vowelStrings(self, words: list[str], queries: list[list[int]]) -> list[int]:
        """
        Counts the number of vowel strings within specified ranges for a given list of words.

        Args:
            words: A list of strings.
            queries: A list of lists, where each inner list represents a query [start, end] (inclusive).
        Returns:
            A list of integers, where each integer is the count of vowel strings for the corresponding query.
        """
        vowels = {'a', 'e', 'i', 'o', 'u'}
        prefixSum = [0] * (len(words) + 1)

        for i in range(len(words)):
            currentWord = words[i]
            if currentWord[0] in vowels and currentWord[-1] in vowels:
                prefixSum[i + 1] = prefixSum[i] + 1
            else:
                prefixSum[i + 1] = prefixSum[i]

        result = []
        for currentQuery in queries:
            start = currentQuery[0]
            end = currentQuery[1]
            result.append(prefixSum[end + 1] - prefixSum[start])

        return result