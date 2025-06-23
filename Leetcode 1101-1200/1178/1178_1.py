# Leetcode 1178: Number of Valid Words for Each Puzzle
# https://leetcode.com/problems/number-of-valid-words-for-each-puzzle/
# Solved on 23rd of June, 2025
from collections import Counter


class Solution:
    def findNumOfValidWords(self, words: list[str], puzzles: list[str]) -> list[int]:
        """
        Finds the number of valid words for each puzzle.

        A word is valid if:
        1. It contains the first letter of the puzzle.
        2. Every letter in the word is also present in the puzzle.

        The solution uses bitmasks to represent words and puzzles for efficient
        checking of letter presence and subsets.

        Args:
            words: A list of words.
            puzzles: A list of puzzles, each 7 letters long.

        Returns:
            A list of integers, where each integer is the count of valid words for the corresponding puzzle.
        """
        def getMask(wordStr: str) -> int:
            mask = 0
            for charVal in set(ord(c) - ord('a') for c in wordStr):
                mask |= (1 << charVal)
            return mask

        wordMaskCounts = Counter()
        for word in words:
            mask = getMask(word)

            if bin(mask).count('1') <= 7:
                wordMaskCounts[mask] += 1

        results = []
        for puzzle in puzzles:
            puzzleMask = getMask(puzzle)

            firstCharPuzzleCode = ord(puzzle[0]) - ord('a')
            firstCharPuzzleBit = (1 << firstCharPuzzleCode)

            currentPuzzleValidWordCount = 0

            subMask = puzzleMask
            while subMask > 0:
                if (subMask & firstCharPuzzleBit) != 0:
                    currentPuzzleValidWordCount += wordMaskCounts[subMask]

                subMask = (subMask - 1) & puzzleMask

            results.append(currentPuzzleValidWordCount)

        return results