# Leetcode 3692: Majority Frequency Characters
# https://leetcode.com/problems/majority-frequency-characters/
# Solved on 17th of October, 2025
from collections import Counter


class Solution:
    def majorityFrequencyGroup(self, s: str) -> str:
        """
        Finds the group of characters that appear with the majority frequency.

        Args:
            s (str): The input string.
        Returns:
            str: A string containing the characters from the majority frequency group, sorted alphabetically.
        """
        # Count frequency of each character
        freq_count = Counter(s)

        # Group characters by their frequency
        freq_groups = {}
        for char, freq in freq_count.items():
            if freq not in freq_groups:
                freq_groups[freq] = []
            freq_groups[freq].append(char)

        # Find the majority frequency group
        max_group_size = 0
        max_frequency = 0
        majority_chars = []

        for freq, chars in freq_groups.items():
            group_size = len(chars)
            if group_size > max_group_size or (group_size == max_group_size and freq > max_frequency):
                max_group_size = group_size
                max_frequency = freq
                majority_chars = chars

        # Return sorted characters from the majority group
        return ''.join(sorted(majority_chars))