# Leetcode 3926: Count Valid Word Occurrences
# https://leetcode.com/problems/count-valid-word-occurrences/
# Solved on 24th of May, 2026
class Solution:
    def countWordOccurrences(self, chunks: list[str], queries:  list[str]) -> list[int]:
        """
        Counts the occurrences of specific query words within a string formed by joining multiple chunks.

        :param chunks: A list of strings that are concatenated to form the source text.
        :param queries: A list of strings representing the words to count in the source text.
        :return: A list of integers where each integer is the frequency of the corresponding query word.
        """
        joinedString = "".join(chunks)
        strLen = len(joinedString)
        wordFreq = {}
        currWord = []

        for i in range(strLen):
            char = joinedString[i]
            if 'a' <= char <= 'z':
                currWord.append(char)
            elif char == '-' and i > 0 and i + 1 < strLen and 'a' <= joinedString[i - 1] <= 'z' and 'a' <= joinedString[i + 1] <= 'z':
                currWord.append(char)
            else:
                if currWord:
                    wordStr = "".join(currWord)
                    wordFreq[wordStr] = wordFreq.get(wordStr, 0) + 1
                    currWord = []

        if currWord:
            wordStr = "".join(currWord)
            wordFreq[wordStr] = wordFreq.get(wordStr, 0) + 1

        ansArray = []
        for queryStr in queries:
            ansArray.append(wordFreq.get(queryStr, 0))

        return ansArray