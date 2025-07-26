# Leetcode 2213: Longest Substring of One Repeating Character
# https://leetcode.com/problems/longest-substring-of-one-repeating-character/
# Solved on 26th of July, 2025
class Solution:
    def longestRepeating(self, s: str, queryCharacters: str, queryIndices: list[int]) -> list[int]:
        """
        Calculates the longest repeating character substring after each query.
        :param s: The initial string.
        :param queryCharacters: A string of characters to replace with.
        :param queryIndices: A list of indices where characters are to be replaced.
        :return: A list of integers, where each integer is the length of the longest repeating character substring after each query.
        """
        class Node:
            def __init__(self):
                self.mx = 0
                self.lmx = 0
                self.rmx = 0
                self.lChar = ''
                self.rChar = ''
                self.size = 0

        n = len(s)
        tree = [Node() for _ in range(4 * n)]

        def pushUp(nodeIndex: int):
            leftNode = tree[2 * nodeIndex + 1]
            rightNode = tree[2 * nodeIndex + 2]
            currentNode = tree[nodeIndex]

            currentNode.size = leftNode.size + rightNode.size
            currentNode.lChar = leftNode.lChar
            currentNode.rChar = rightNode.rChar

            currentNode.lmx = leftNode.lmx
            if leftNode.lmx == leftNode.size and leftNode.rChar == rightNode.lChar:
                currentNode.lmx += rightNode.lmx

            currentNode.rmx = rightNode.rmx
            if rightNode.rmx == rightNode.size and rightNode.lChar == leftNode.rChar:
                currentNode.rmx += leftNode.rmx

            currentNode.mx = max(leftNode.mx, rightNode.mx)
            if leftNode.rChar == rightNode.lChar:
                currentNode.mx = max(currentNode.mx, leftNode.rmx + rightNode.lmx)

        def build(nodeIndex: int, start: int, end: int):
            if start == end:
                node = tree[nodeIndex]
                node.mx = 1
                node.lmx = 1
                node.rmx = 1
                node.lChar = s[start]
                node.rChar = s[start]
                node.size = 1
                return

            mid = (start + end) // 2
            build(2 * nodeIndex + 1, start, mid)
            build(2 * nodeIndex + 2, mid + 1, end)
            pushUp(nodeIndex)

        def update(nodeIndex: int, start: int, end: int, queryIndex: int, newChar: str):
            if start == end:
                node = tree[nodeIndex]
                node.lChar = newChar
                node.rChar = newChar
                return

            mid = (start + end) // 2
            if queryIndex <= mid:
                update(2 * nodeIndex + 1, start, mid, queryIndex, newChar)
            else:
                update(2 * nodeIndex + 2, mid + 1, end, queryIndex, newChar)
            pushUp(nodeIndex)

        build(0, 0, (n - 1))

        results = []
        numQueries = len(queryIndices)
        for i in range(numQueries):
            idx = queryIndices[i]
            char = queryCharacters[i]
            update(0, 0, (n - 1), idx, char)
            results.append(tree[0].mx)

        return results