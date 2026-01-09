# Leetcode 3799: Word Squares II
# https://leetcode.com/problems/word-squares-ii/
# Solved on 9th of January, 2026
class Solution:
    def wordSquares(self, words: list[str]) -> list[list[str]]:
        """
        This function finds all possible word squares from a given list of words.
        :param words: A list of strings, where each string is a word.
        :return: A list of lists of strings, where each inner list represents a valid word square.
        """
        words.sort()
        n = len(words)

        resultList = []
        for i in range(n):
            top = words[i]

            for j in range(n):
                if i == j:
                    continue

                left = words[j]
                if top[0] != left[0]:
                    continue

                for k in range(n):
                    if k == i or k == j:
                        continue

                    right = words[k]
                    if top[3] != right[0]:
                        continue

                    for l in range(n):
                        if l == i or l == j or l == k:
                            continue

                        bottom = words[l]
                        if bottom[0] == left[3] and bottom[3] == right[3]:
                            resultList.append([top, left, right, bottom])

        return resultList