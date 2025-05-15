# Leetcode 2900: Longest Unequal Adjacent Groups Subsequence I
# https://leetcode.com/problems/longest-unequal-adjacent-groups-subsequence-i/
# Solved on 15th of May, 2025

class Solution:
    def getLongestSubseqence(self, words: list[str], groups: list[int]) -> list[str]:
        """
        Given a list of words and their corresponding groups, this function returns the longest subsequence
        of words such that no two adjacent words in the subsequence belong to the same group.

        Args:
            words (list[str]): A list of words.
            groups (list[int]): A list of integers representing the group of each word.

        Returns:
            list[str]: The longest subsequence of words with unequal adjacent groups.
        """

        n = len(words)

        # Handle the edge case of an empty input list
        if n == 0:
            return []

        # Initialize the subsequence with the first word.
        # The first word is always part of a candidate longest subsequence built this way.
        longest_subsequence = [words[0]]

        # Keep track of the group of the last word added to our subsequence
        last_group_in_subsequence = groups[0]

        # Iterate through the rest of the words starting from the second word (index 1).
        for i in range(1, n):
            current_word = words[i]
            current_group = groups[i]

            # If the current word's group is different from the group of the last word added to the subsequence,
            # then this word can extend the alternating subsequence
            if current_group != last_group_in_subsequence:
                longest_subsequence.append(current_word)
                # Update the last group in the subsequence to the current group
                last_group_in_subsequence = current_group

        return longest_subsequence