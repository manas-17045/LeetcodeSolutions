# Leetcode 1754: Largest Merge Of Two Strings
# https://leetcode.com/problems/largest-merge-of-two-strings/
# Solved on 19th of November, 2025
class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        """
        Given two strings word1 and word2, return the largest merge of the two strings.
        A merge is created by repeatedly appending the lexicographically largest available character
        from either word1 or word2.
        :param word1: The first string.
        :param word2: The second string.
        :return: The largest merge of the two strings.
        """
        mergeResult = []
        while word1 and word2:
            if word1 >= word2:
                mergeResult.append(word1[0])
                word1 = word1[1:]
            else:
                mergeResult.append(word2[0])
                word2 = word2[1:]
        mergeResult.append(word1)
        mergeResult.append(word2)
        return "".join(mergeResult)