# Leetcode 2416: Sum of Prefix Scores of Strings
# https://leetcode.com/problems/sum-of-prefix-scores-of-strings/
# Solved on 29th of June, 2025
import collections


class TrieNode:
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.count = 0

class Solution:
    def sumPrefixScores(self, words: list[str]) -> list[int]:
        """
        Calculates the sum of prefix scores for each word in a given list.

        A prefix score for a word is the sum of counts of all its prefixes
        in the Trie.

        Args:
            words: A list of strings.
        Returns:
            A list of integers, where each integer is the prefix score for the corresponding word.
        """
        root = TrieNode()

        for word in words:
            currentNode = root
            for char in word:
                currentNode = currentNode.children[char]
                currentNode.count += 1

        answer = []
        for word in words:
            currentScore = 0
            currentNode = root
            for char in word:
                currentNode = currentNode.children[char]
                currentScore += currentNode.count
            answer.append(currentScore)

        return answer