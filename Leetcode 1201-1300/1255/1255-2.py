# Leetcode 1255: Maximum Score Words Formed by Letters
# https://leetcode.com/problems/maximum-score-words-formed-by-letters/
# Solved on 10th of September, 2025
class Solution:
    def maxScoreWords(self, words: list[str], letters: list[str], score: list[int]) -> int:
        """
        Calculates the maximum score that can be obtained by forming words from a given set of letters.

        Args:
            words (list[str]): A list of words that can be formed.
            letters (list[str]): A list of available letters.
            score (list[int]): A list where score[i] is the score of the i-th letter ('a' through 'z').
        Returns:
            int: The maximum score that can be obtained.
        """
        n = len(words)
        # Precompute counts and score for each word
        word_counts = [[0] * 26 for _ in range(n)]
        word_score = [0] * n
        for i, w in enumerate(words):
            s = 0
            wc = word_counts[i]
            for ch in w:
                idx = ord(ch) - 97
                wc[idx] += 1
                s += score[idx]
            word_score[i] = s

        # Available letters count
        letters_count = [0] * 26
        for ch in letters:
            letters_count[ord(ch) - 97] += 1

        full = 1 << n
        counts_mask = [None] * full
        counts_mask[0] = [0] * 26
        valid = [False] * full
        valid[0] = True
        mask_score = [0] * full
        max_score = 0

        for mask in range(1, full):
            prev = mask & (mask - 1)  # mask without the lowest set bit
            last_bit = mask ^ prev  # the lowest set bit
            word_idx = last_bit.bit_length() - 1

            prev_counts = counts_mask[prev]
            # Build new counts by adding word_counts[word_idx] to prev_counts
            new_counts = prev_counts[:]
            wc = word_counts[word_idx]
            over = False
            for c in range(26):
                new_counts[c] += wc[c]
                # Early check against available letters
                if new_counts[c] > letters_count[c]:
                    over = True
                    break

            if over:
                counts_mask[mask] = new_counts
                valid[mask] = False
            else:
                counts_mask[mask] = new_counts
                valid[mask] = True
                mask_score[mask] = mask_score[prev] + word_score[word_idx]
                if mask_score[mask] > max_score:
                    max_score = mask_score[mask]

        return max_score