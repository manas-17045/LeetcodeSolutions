# Leetcode 2416: Sum of Prefix Scores of Strings
# https://leetcode.com/problems/sum-of-prefix-scores-of-strings/
# Solved on 29th of June, 2025
class TrieNode:
    __slots__ = ('count', 'children')

    def __init__(self):
        # Number of words sharing the prefix leading to this node
        self.count = 0
        # Child links for each lowercase letter
        self.children = {}


class Solution:
    def sumPrefixScores(self, words: list[str]) -> list[int]:
        """
        Calculates the sum of prefix scores for each word in a given list.

        The score of a prefix is defined as the number of words in the input list
        that have this prefix. The total score for a word is the sum of scores
        of all its prefixes.

        Args:
            words: A list of strings (words).

        Returns:
            A list of integers, where each integer is the total prefix score
            for the corresponding word in the input list.
        """
        # Build the Trie
        root = TrieNode()
        for word in words:
            node = root
            for ch in word:
                if ch not in node.children:
                    node.children[ch] = TrieNode()
                node = node.children[ch]
                node.count += 1

        # For each word, sum the counts on its path
        ans = []
        for word in words:
            node = root
            total = 0
            for ch in word:
                node = node.children[ch]
                total += node.count
            ans.append(total)

        return ans
