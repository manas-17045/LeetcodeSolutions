# Leetcode 2131: Longest Palindrome by Concatenating Two Letter Words
# https://leetcode.com/problems/longest-palindrome-by-concatenating-two-letter-words/
# Solved on 25th of May, 2025
import collections


class Solution:
    def longestPalindrome(self, words: list[str]) -> int:
        """
        Finds the length of the longest palindrome that can be built by concatenating two-letter words.

        A palindrome can be formed by pairing words with their reverses (e.g., "lc" and "cl")
        and potentially placing a single word that is a palindrome itself (e.g., "gg") in the center
        if there's an odd count of such a word.

        Args:
            words: A list of strings, where each string is a two-letter word.

        Returns:
            The length of the longest palindrome that can be formed.

        """

        counts = collections.Counter(words)
        length = 0
        # This flag will be true if we find any word of the form "aa", "bb", etc.
        # (a palindrome itself) that has an odd count. Such a word can be placed
        # in the center of the final palindrome.
        center_candidate_present = False

        for word, count_of_word in counts.items():
            # word is a string of 2 characters, e.g., "lc" or "gg"
            # count_of_word is its frequency in the input `words` list
            char1 = word[0]
            char2 = word[1]

            if char1 == char2:  # Word is of the form "aa", "bb", etc.
                # We can use pairs of this word (e.g., "gg" and "gg") to extend the palindrome symmetrically.
                # Each such pair ("gg", "gg") forms "gggg", contributing 4 to the total length.
                # We can form (count_of_word // 2) such pairs.
                length += (count_of_word // 2) * 4

                if count_of_word % 2 == 1:
                    # If there's an odd number of this word (e.g., three "gg"s),
                    # one "gg" is left over after forming pairs.
                    # This leftover "gg" can be placed in the center of the palindrome.
                    center_candidate_present = True
            else:   # Word is of the form "ab" where a != b (e.g., "lc")
                reversed_word = char2 + char1     # e.g., if word is "lc", reversed_word is "cl"

                # To avoid double counting pairs (e.g., considering "lc"-"cl" and later "cl"-"lc"),
                # we only process the pair if `word` is lexicographically smaller than `reversed_word`.
                if word < reversed_word:
                    if reversed_word in counts:
                        count_of_revered_word = counts[reversed_word]

                        # We can form `num_formations` instances of "word ... reversed_word".
                        # Each formation uses one `word` and one `reversed_word`.
                        # Each such formation adds 4 to the length (2 for `word`, 2 for `reversed_word`).
                        num_formations = min(count_of_word, count_of_revered_word)
                        length += num_formations * 4

        # If `center_candidate_present` is true, we can place one "xx"-type word
        # (that had an odd count) in the absolute center of our palindrome.
        # This adds 2 to the total length (since each word has length 2).
        if center_candidate_present:
            length += 2

        return length