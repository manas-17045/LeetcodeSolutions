# Leetcode 2901: Longest Unequal Adjacent Groups Subsequence II
# https://leetcode.com/problems/longest-unequal-adjacent-groups-subsequence-ii/
# Solved on 16th of May, 2025

class Solution:
    def getWordsInLongestSubsequence(self, words: list[str], groups: list[int]) -> list[str]:
        """
        Finds the longest subsequence of words such that adjacent words have different groups and a Hamming distance of 1.

        Args:
            words: A list of strings representing the words.
            groups: A list of integers representing the group each word belongs to.

        Returns: A list of strings representing the words in the longest subsequence.
        """
        n = len(words)

        if n == 0:
            return []

        # dp[i] stores the length of the longest valid subsequence ending at index i
        dp = [1] * n
        # parent[i] stores the index of the predecessor of i in such a subsequence.
        parent = [-1] * n

        # The minimum longest subsequence is of length 1.
        max_len = 1
        # max_len_end_idx stores the index where the current longest subsequence ends.
        # Initialize to 0, as if n = 1, the subsequence is words[0] ending at index 0.
        max_len_end_idx = 0

        for i in range(n):
            # For each word i, try to extend subsequences ending at previous words j.
            for j in range(i):

                # Condition 1: Groups must be unequal.
                if groups[j] == groups[i]:
                    continue

                word_j = words[j]
                word_i = words[i]

                # Condition 2: Word lengths must be equal.
                if len(word_j) != len(word_i):
                    continue

                # Condition 3: Hamming distance must be 1.
                # Calculate Hamming distance. Max word length L is 10.
                hamming_dist = 0
                # Loop runs L times (length of the words).
                for k in range(len(word_j)):
                    if word_j[k] != word_i[k]:
                        hamming_dist += 1

                if hamming_dist == 1:
                    # All conditions met, words[j] can precede words[j].
                    # If extending the subsequence ending at j creates a longer
                    # subsequence for i than currently known:
                    if dp[j] + 1 > dp[i]:
                        dp[i] = dp[j] + 1
                        parent[i] = j

            # After checking all possible predecessors j for the current i:
            # If the subsequence ending at i is longer than any found so far, update max_len.
            if dp[i] > max_len:
                max_len = dp[i]
                max_len_end_idx = i

        # Reconstruct the longest subsequence using parent pointers.
        # Start from max_len_end_idx and backtrack
        longest_subsequence_indices = []
        curr_idx = max_len_end_idx
        while curr_idx != -1:
            longest_subsequence_indices.append(curr_idx)
            curr_idx = parent[curr_idx]

        # The indices were added in reverse order (end to start). Reverse to get the correct order.
        longest_subsequence_indices.reverse()

        # Map indices to the actual words
        result_words = [words[idx] for idx in longest_subsequence_indices]

        return result_words