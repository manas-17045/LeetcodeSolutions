# Leetcode 2135: Count Words Obtained After Adding a Letter
# https://leetcode.com/problems/count-words-obtained-after-adding-a-letter/
# Solved on 23rd of July, 2025
class Solution:
    def wordCount(self, startWords: list[str], targetWords: list[str]) -> int:
        """
        Counts how many target words can be formed by adding exactly one letter to a start word.

        Args:
            startWords: A list of strings representing the initial set of words.
            targetWords: A list of strings representing the words to check against.

        Returns:
            The number of target words that can be formed from a start word by adding one letter.
        """
        # Helper function to turn a word into a 26-bit mask
        def mask(word: str) -> int:
            m = 0
            for ch in word:
                m |= 1 << (ord(ch) - ord('a'))
            return m

        start_masks = set(mask(w) for w in startWords)
        ans = 0

        for w in targetWords:
            m = mask(w)
            # Try removing each letter in w.
            # If after removal, we get a mask seen in start_masks, count this target.
            bit = m
            while bit:
                # Isolate lowest set bit
                low = bit & -bit
                cand = m ^ low  # Remove that one letter
                if cand in start_masks:
                    ans += 1
                    break
                bit ^= low  # Remove that bit and continue

        return ans