# Leetcode 3302: Find the Lexicographically Smallest Valid Sequence
# https://leetcode.com/problems/find-the-lexicographically-smallest-valid-sequence/
# Solved on 30th of August, 2025
class Solution:
    def validSequence(self, word1: str, word2: str) -> list[int]:
        """
        This function finds a valid sequence of indices from word1 that forms word2, allowing for one skipped character in word2.
        :param word1: The first string.
        :param word2: The second string, which is a subsequence of word1 with at most one character skipped.
        :return: A list of integers representing the indices from word1 that form word2, or an empty list if no such sequence exists.
        """
        if not word2:
            return []

        m = len(word2)
        last = [-1] * m
        i = len(word1) - 1
        j = m - 1

        while i >= 0 and j >= 0:
            if word1[i] == word2[j]:
                last[j] = i
                j -= 1
            i -= 1

        ans = []
        can_skip = True
        j = 0
        for i in range(len(word1)):
            if j == m:
                break

            if word1[i] == word2[j]:
                ans.append(i)
                j += 1
            elif can_skip and (j == (m - 1) or i < last[j + 1]):
                ans.append(i)
                can_skip = False
                j += 1

        return ans if j == m else []