# Leetcode 3775: Reverse Words With Same Vowel Count
# https://leetcode.com/problems/reverse-words-with-same-vowel-count/
# Solved on 25th of December, 2025
class Solution:
    def reverseWords(self, s: str) -> str:
        """
        Reverses words in a string that have the same vowel count as the first word.

        Args:
            s (str): The input string containing words separated by spaces.
        Returns:
            str: The modified string with relevant words reversed.
        """
        words = s.split(' ')
        vowels = {'a', 'e', 'i', 'o', 'u'}

        def countVowels(word):
            count = 0
            for char in word:
                if char in vowels:
                    count += 1
            return count

        targetCount = countVowels(words[0])

        for i in range(1, len(words)):
            if countVowels(words[i]) == targetCount:
                words[i] = words[i][::-1]

        return " ".join(words)