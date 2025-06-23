# Leetcode 1178: Number of Valid Words for Each Puzzle
# https://leetcode.com/problems/number-of-valid-words-for-each-puzzle/
# Solved on 23rd of June, 2025
from collections import Counter


class Solution:
    def findNumOfValidWords(self, words: list[str], puzzles: list[str]) -> list[int]:
        """
        Given a list of words and a list of puzzles, return the number of valid words for each puzzle.
        A word is valid for a given puzzle if:
        1. The word contains the first letter of the puzzle.
        2. Every letter in the word is also in the puzzle.
        3. The word contains at most 7 unique letters.
        """
        # Build a frequency map of word bitmasks. ignoring words with > 7 distinct letters.
        word_mask_count = Counter()
        for w in words:
            m = 0
            for ch in set(w):
                m |= 1 << (ord(ch) - ord('a'))
            # Only words with at most 7 distinct letters could ever match a 7-letter puzzle
            if m.bit_count() <= 7:
                word_mask_count[m] += 1

        ans = []
        # For each puzzle, enumerate all subsets of its last 6 letters, force-include the first letter bit in every
        # subset-mask, and sum matches.
        for p in puzzles:
            first_bit = 1 << (ord(p[0]) - ord('a'))
            # Get bit indices for thr other 6 letters
            others = [ord(ch) - ord('a') for ch in p[1:]]

            total = 0
            # There are 2^6 subsets of the oter letters
            for subset in range(1 << 6):
                mask = first_bit
                # Add in bits for those positions present in this subset
                for i in range(6):
                    if subset & (1 << i):
                        mask |= 1 << others[i]
                total += word_mask_count.get(mask, 0)
            ans.append(total)

        return ans