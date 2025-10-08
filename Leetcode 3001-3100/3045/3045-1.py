# Leetcode 3045: Count Prefix and Suffix Pairs II
# https://leetcode.com/problems/count-prefix-and-suffix-pairs-ii/
# Solved on 8th of October, 2025
class Solution:
    def countPrefixSuffixPairs(self, words: list[str]) -> int:
        """
        Counts the number of pairs (i, j) such that i < j, and words[i] is both a prefix and a suffix of words[j].

        Args:
            words: A list of strings.
        Returns:
            The total number of such pairs.
        """
        class TrieNode:
            def __init__(self):
                self.children = {}
                self.count = 0

        trieRoot = TrieNode()
        totalCount = 0

        for word in words:
            currentNode = trieRoot
            wordLength = len(word)

            for i in range(wordLength):
                key = (word[i], word[wordLength - 1 - i])
                if key not in currentNode.children:
                    break
                currentNode = currentNode.children[key]
                totalCount += currentNode.count

            currentNode = trieRoot
            for i in range(wordLength):
                key = (word[i], word[wordLength - 1 - i])
                if key not in currentNode.children:
                    currentNode.children[key] = TrieNode()
                currentNode = currentNode.children[key]
            currentNode.count += 1

        return totalCount