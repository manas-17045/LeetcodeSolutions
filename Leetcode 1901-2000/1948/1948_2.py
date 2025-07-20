# Leetcode 1948: Delete Duplicate Folders in System
# https://leetcode.com/problems/delete-duplicate-folders-in-system/
# Solved on 20th of July, 2025
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_deleted = False

class Solution:
    def deleteDuplicateFolder(self, paths: list[list[str]]) -> list[list[str]]:
        """
        Deletes duplicate folder structures from a given list of paths.
        :param paths: A list of paths, where each path is a list of strings representing folder names.
        :return: A list of paths after deleting duplicate folder structures.
        """
        root = TrieNode()

        # Build the Trie
        for path in paths:
            node = root
            for name in path:
                if name not in node.children:
                    node.children[name] = TrieNode()
                node = node.children[name]

        lookup = {}
        def serialize(node: TrieNode) -> str:
            # Leaf node
            if not node.children:
                return ""

            # For each child, create a tuple (name, serialization)
            serials = []
            for name in sorted(node.children):
                child_serial = serialize(node.children[name])
                serials.append(f"({name}{child_serial})")
            # Full serialization of subtree
            serial = ''.join(serials)
            # Put in lookup to detect duplicates
            if serial not in lookup:
                lookup[serial] = []
            lookup[serial].append(node)
            return serial

        serialize(root)

        # Mark duplicate subtrees as `deleted`
        for nodes in lookup.values():
            if len(nodes) > 1:
                for n in nodes:
                    n.is_deleted = True

        # DFS to recover all valid paths
        res = []
        def collect(node: TrieNode, path: list[str]):
            if node.is_deleted:
                return
            for name, child in node.children.items():
                collect(child, path + [name])
                if not child.is_deleted:
                    res.append(path + [name])

        collect(root, [])
        return res