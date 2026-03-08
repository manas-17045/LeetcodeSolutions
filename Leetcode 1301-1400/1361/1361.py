# Leetcode 1361: Validate Binary Tree Nodes
# https://leetcode.com/problems/validate-binary-tree-nodes/
# Solved on 8th of March, 2026
import collections


class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: list[int], rightChild: list[int]) -> bool:
        """
        Validates if n nodes form exactly one valid binary tree.

        :param n: The number of nodes labeled from 0 to n - 1.
        :param leftChild: A list where leftChild[i] is the left child of node i.
        :param rightChild: A list where rightChild[i] is the right child of node i.
        :return: True if the nodes form a single valid binary tree, False otherwise.
        """
        inDegree = [0] * n

        for i in range(n):
            leftNode = leftChild[i]
            rightNode = rightChild[i]

            if leftNode != -1:
                inDegree[leftNode] += 1
                if inDegree[leftNode] > 1:
                    return False

            if rightNode != -1:
                inDegree[rightNode] += 1
                if inDegree[rightNode] > 1:
                    return False

        rootNode = -1
        for i in range(n):
            if inDegree[i] == 0:
                if rootNode != -1:
                    return False
                rootNode = i

        if rootNode == -1:
            return False

        visitedNodes = {rootNode}
        nodeQueue = collections.deque([rootNode])

        while nodeQueue:
            currentNode = nodeQueue.popleft()
            leftNode = leftChild[currentNode]
            rightNode = rightChild[currentNode]

            if leftNode != -1:
                if leftNode in visitedNodes:
                    return False
                visitedNodes.add(leftNode)
                nodeQueue.append(leftNode)

            if rightNode != -1:
                if rightNode in visitedNodes:
                    return False
                visitedNodes.add(rightNode)
                nodeQueue.append(rightNode)

        return len(visitedNodes) == n