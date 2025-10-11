# Leetcode 3291: Minimum Number of Valid Strings to Form Target I
# https://leetcode.com/problems/minimum-number-of-valid-strings-to-form-target-i/
# Resolved on 11th of October, 2025
class Solution:
    def minValidStrings(self, words: list[str], target: str) -> int:
        """
        Calculates the minimum number of valid strings from `words` needed to form the `target` string.

        Args:
            words: A list of strings that can be used to form the target.
            target: The target string to be formed.
        Returns:
            The minimum number of valid strings, or -1 if the target cannot be formed.
        """
        class TrieNode:
            def __init__(self):
                self.children = {}

        rootNode = TrieNode()
        for word in words:
            currentNode = rootNode
            for char in word:
                if char not in currentNode.children:
                    currentNode.children[char] = TrieNode()
                currentNode = currentNode.children[char]

        targetLength = len(target)
        dp = [float('inf')] * (targetLength + 1)
        dp[0] = 0

        for i in range(targetLength):
            if dp[i] == float('inf'):
                continue

            currentNode = rootNode
            for j in range(i, targetLength):
                currentChar = target[j]

                if currentChar not in currentNode.children:
                    break

                currentNode = currentNode.children[currentChar]
                dp[j + 1] = min(dp[j + 1], dp[i] + 1)

        finalResult = dp[targetLength]

        return int(finalResult) if finalResult != float('inf') else -1