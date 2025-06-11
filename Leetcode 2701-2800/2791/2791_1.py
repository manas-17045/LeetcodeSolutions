# Leetcode 2791: Count Paths That Can Form a Palindrome in a Tree
# https://leetcode.com/problems/count-paths-that-can-form-a-palindrome-in-a-tree/
# Solved on 11th of June, 2025
from collections import defaultdict, Counter


class Solution:
    def countPalindromePaths(self, parent: list[int], s: str) -> int:
        """
        Counts the number of paths in a tree that can form a palindrome.

        A path can form a palindrome if the count of each character in the path
        is even, with at most one character having an odd count. This can be
        represented using a bitmask, where each bit corresponds to a character
        ('a' to 'z'), and the bit is set if the character appears an odd number
        of times in the path from the root to the current node.

        Args:
            parent: A list representing the parent of each node. parent[i] is the parent of node i.
            s: A string where s[i] is the character at node i.

        Returns:
            The total number of paths that can form a palindrome.
        """
        nodeCount = len(parent)
        adjacencyList = defaultdict(list)
        for i in range(1, nodeCount):
            adjacencyList[parent[i]].append(i)

        pathMasks = {}
        stack = [(0, 0)]

        while stack:
            currentNode, currentMask = stack.pop()
            pathMasks[currentNode] = currentMask

            for neighborNode in adjacencyList[currentNode]:
                charIndex = ord(s[neighborNode]) - ord('a')
                neighborMask = currentMask ^ (1 << charIndex)
                stack.append((neighborNode, neighborMask))

        maskFrequencies = Counter(pathMasks.values())

        palindromePathCount = 0

        for maskValue, frequency in maskFrequencies.items():
            palindromePathCount += frequency * (frequency - 1) // 2

            for i in range(26):
                targetMask = maskValue ^ (1 << i)
                if targetMask > maskValue and targetMask in maskFrequencies:
                    palindromePathCount += frequency * maskFrequencies[targetMask]

        return palindromePathCount