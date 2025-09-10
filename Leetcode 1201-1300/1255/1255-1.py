# Leetcode 1255: Maximum Score Words Formed by Letters
# https://leetcode.com/problems/maximum-score-words-formed-by-letters/
# Solved on 10th of September, 2025
import collections


class Solution:
    def maxScoreWords(self, words: list[str], letters: list[str], score: list[int]) -> int:
        """
        Calculates the maximum score achievable by forming words from a given set of letters.

        Args:
            words (list[str]): A list of words that can be formed.
            letters (list[str]): A list of available letters.
            score (list[int]): A list where score[i] is the score of the i-th letter of the alphabet.

        Returns:
            int: The maximum score that can be achieved.
        """
        lettersCount = collections.Counter(letters)

        def backtrack(index):
            if index == len(words):
                return 0

            maxScore = backtrack(index + 1)

            word = words[index]
            wordCount = collections.Counter(word)

            isPossible = True
            for char, count in wordCount.items():
                if lettersCount[char] < count:
                    isPossible = False
                    break

            if isPossible:
                currentWordScore = 0
                for char, count in wordCount.items():
                    lettersCount[char] -= count
                    currentWordScore += score[ord(char) - ord('a')] * count

                newTotalScore = currentWordScore + backtrack(index + 1)
                maxScore = max(maxScore, newTotalScore)

                for char, count in wordCount.items():
                    lettersCount[char] += count

            return maxScore

        return backtrack(0)