# Leetcode 3045: Count Prefix and Suffix Pairs II
# https://leetcode.com/problems/count-prefix-and-suffix-pairs-ii/
# Solved on 8th of October, 2025
class Solution:
    def countPrefixSuffixPairs(self, words: list[str]) -> int:
        """
        Counts the number of pairs (i, j) such that i < j and words[i] is both a prefix and a suffix of words[j].

        Args:
            words: A list of strings.
        Returns:
            The total count of such pairs.
        """
        class TrieNode:
            def __init__(self):
                self.children = {}
                self.count = 0

        class Trie:
            def __init__(self):
                self.root = TrieNode()

            def insert(self, word):
                node = self.root
                n = len(word)
                for i in range(n):
                    pair = (word[i], word[n - 1 - i])
                    if pair not in node.children:
                        node.children[pair] = TrieNode()
                    node = node.children[pair]
                node.count += 1

            def count_matches(self, word):
                count = 0
                node = self.root
                n = len(word)

                for i in range(n):
                    pair = (word[i], word[n - 1 - i])
                    if pair not in node.children:
                        break
                    node = node.children[pair]
                    count += node.count

                return count

        trie = Trie()
        result = 0

        for word in words:
            # Count how many previous words are both prefix and suffix of current word
            result += trie.count_matches(word)
            # Insert current word into trie
            trie.insert(word)

        return result