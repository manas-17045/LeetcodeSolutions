# Leetcode 1948: Delete Duplicate Folders in System
# https://leetcode.com/problems/delete-duplicate-folders-in-system/
# Solved on 20th of July, 2025
import collections


class Solution:
    def deleteDuplicateFolder(self, paths: list[list[str]]) -> list[list[str]]:
        """
        Deletes duplicate folder structures from a file system represented by paths.

        Args:
            paths: A list of lists of strings, where each inner list represents a path to a folder.
        Returns:
            A list of lists of strings, representing the remaining paths after deleting duplicate folder structures.
        """

        class TrieNode:
            def __init__(self):
                self.children = {}
                self.isDeleted = False

        root = TrieNode()
        # Build the Trie from the input paths
        for path in paths:
            node = root
            for folderName in path:
                if folderName not in node.children:
                    node.children[folderName] = TrieNode()
                node = node.children[folderName]

        seenStructures = collections.defaultdict(list)

        # Serialize each subtree into a hashable tuple and find duplicates
        def serialize(node: TrieNode) -> tuple:
            # A leaf node's structure is represented by an empty tuple
            if not node.children:
                return tuple()

            # Recursively get signatures for all children
            childStructures = []
            for name, childNode in sorted(node.children.items()):
                childStructures.append((name, serialize(childNode)))

            # The signature for the currentNode's structure is a tuple of its children's signature.
            structureTuple = tuple(childStructures)

            # If the folder is not empty, record its structure
            if structureTuple:
                seenStructures[structureTuple].append(node)

            return structureTuple

        serialize(node)

        # Mark all nodes that are part of a duplicate structure
        for nodes in seenStructures.values():
            if len(nodes) > 1:
                for node in nodes:
                    node.isDeleted = True

        result = []

        # Traverse the Trie agin to build the final list of paths, skipping deleted nodes
        def buildResult(node: TrieNode, currentPath: list[str]):
            for name, childNode in sorted(node.children.items()):
                if not childNode.isDeleted:
                    newPath = currentPath + [name]
                    result.append(newPath)
                    buildResult(childNode, newPath)

        buildResult(root, [])

        return result