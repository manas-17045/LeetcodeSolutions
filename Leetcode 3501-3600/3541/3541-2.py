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
        # Frequency array for 'a'...'z'
        freq = [0] * 26
        base = ord('a')
        for ch in s:
            freq[ord(ch) - base] += 1

        # Vowel indices: a, e, i, o, u
        vowel_idxs = (ord('a') - base,
                      ord('e') - base,
                      ord('i') - base,
                      ord('o') - base,
                      ord('u') - base
                      )
        max_vowel = 0
        for idx in vowel_idxs:
            if freq[idx] > max_vowel:
                max_vowel = freq[idx]

        # Consonants: all other indices 0...25 excluding vowel indices
        vowel_set = set(vowel_idxs)
        max_consonant = 0
        for i in range(26):
            if i in vowel_set:
                continue
            if freq[i] > max_consonant:
                max_consonant = freq[i]

        return max_vowel + max_consonant