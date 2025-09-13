# Leetcode 3541: Find Most Frequent Vowel and Consonant
# https://leetcode.com/problems/find-most-frequent-vowel-and-consonant/
# Solved on 13th of September, 2025
class Solution:
    def maxFreqSum(self, s: str) -> int:
        """
        Calculates the sum of the maximum frequency of a vowel and the maximum frequency of a consonant in a given string.

        :param s: The input string consisting of lowercase English letters.
        :return: The sum of the maximum frequency of a vowel and the maximum frequency of a consonant.
        """
        charFrequencies = [0] * 26
        for char in s:
            charFrequencies[ord(char) - ord('a')] += 1

        maxVowelFrequency = 0
        maxConsonantFrequency = 0
        vowels = "aeiou"

        for i in range(26):
            character = chr(ord('a') + i)
            frequency = charFrequencies[i]

            if character in vowels:
                if frequency > maxVowelFrequency:
                    maxVowelFrequency = frequency
            else:
                if frequency > maxConsonantFrequency:
                    maxConsonantFrequency = frequency

        return maxVowelFrequency + maxConsonantFrequency