# Leetcode 3093: Longest Common Suffix Queries
# https://leetcode.com/problems/longest-common-suffix-queries/
# Solved on 24th of August, 2025
class _TrieNode:
    __slots__ = ("children", "best")

    def __init__(self):
        self.children = {}  # char -> _TrieNode
        self.best = -1  # index in wordsContainer of the best candidate for this node


class Solution:
    def stringIndices(self, wordsContainer: list[str], wordsQuery: list[str]) -> list[int]:
        """
        Finds the best matching word index from wordsContainer for each query in wordsQuery.

        Args:
            wordsContainer (list[str]): A list of words to search within.
            wordsQuery (list[str]): A list of query strings.
        Returns:
            list[int]: A list of indices, where each index corresponds to the best matching word
                       from wordsContainer for the respective query in wordsQuery.
        """
        if not wordsContainer:
            return [-1] * len(wordsQuery)

        # Precompute lengths for quick comparisons
        lengths = [len(w) for w in wordsContainer]

        def better_index(i: int, j: int) -> int:
            if i == -1:
                return j
            if j == -1:
                return i
            li, lj = lengths[i], lengths[j]
            if li < lj:
                return i
            if li > lj:
                return j
            return i if i < j else j

        # Build reversed trie
        root = _TrieNode()
        for idx, word in enumerate(wordsContainer):
            node = root
            # Update root candidate
            node.best = better_index(node.best, idx)
            # Insert reversed characters
            for ch in reversed(word):
                if ch not in node.children:
                    node.children[ch] = _TrieNode()
                node = node.children[ch]
                node.best = better_index(node.best, idx)

        # Querying: traverse reversed query and use the best stored at deepest node reached
        result = []
        for q in wordsQuery:
            node = root
            for ch in reversed(q):
                if ch in node.children:
                    node = node.children[ch]
                else:
                    break
            result.append(node.best)
        return result
