# Leetcode 2452: Words Within Two Edits of Dictionary
# https://leetcode.com/problems/words-within-two-edits-of-dictionary/
# Solved on 22nd of April, 2026
class Solution:
    def twoEditWords(self, queries: list[str], dictionary: list[str]) -> list[str]:
        """
        Finds all words from queries that are within two edits of any word in the dictionary.

        :param queries: A list of strings representing the words to check.
        :param dictionary: A list of strings representing the reference dictionary.
        :return: A list of strings from queries that satisfy the two-edit condition.
        """
        validQueries = []

        for queryWord in queries:
            for dictWord in dictionary:
                diffCount = 0
                for i in range(len(queryWord)):
                    if queryWord[i] != dictWord[i]:
                        diffCount += 1
                        if diffCount > 2:
                            break

                if diffCount <= 2:
                    validQueries.append(queryWord)
                    break

        return validQueries