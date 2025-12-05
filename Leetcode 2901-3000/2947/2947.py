# Leetcode 2947: Count Beautiful Substrings I
# https://leetcode.com/problems/count-beautiful-substrings-i/
# Solved on 5th of December, 2025
class Solution:
    def beautifulSubstrings(self, s: str, k: int) -> int:
        """
        Counts the number of beautiful substrings in a given string s.

        :param s: The input string.
        :param k: An integer for the divisibility condition.
        :return: The total count of beautiful substrings.
        """
        length = len(s)
        vowelSet = {'a', 'e', 'i', 'o', 'u'}
        result = 0

        for i in range(length):
            vowels = 0
            consonants = 0
            for j in range(i, length):
                if s[j] in vowelSet:
                    vowels += 1
                else:
                    consonants += 1
                if vowels == consonants and (vowels * consonants) % k == 0:
                    result += 1

        return result