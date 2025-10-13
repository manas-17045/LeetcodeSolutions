# Leetcode 2273: Find Resultant Array After Removing Anagrams
# https://leetcode.com/problems/find-resultant-array-after-removing-anagrams/
# Solved on 13th of October, 2025
class Solution:
    def removeAnagrams(self, words: list[str]) -> list[str]:
        """
        Removes consecutive anagrams from a list of words.
        :param words: A list of strings.
        :return: A list of strings with consecutive anagrams removed.
        """
        result = []
        prev_sorted = None

        for word in words:
            sorted_word = ''.join(sorted(word))

            # Only add if it's not an anagram of the previous word
            if sorted_word != prev_sorted:
                result.append(word)
                prev_sorted = sorted_word

        return result