# Leetcode 2213: Longest Substring of One Repeating Character
# https://leetcode.com/problems/longest-substring-of-one-repeating-character/
# Solved on 26th of July, 2025
class SegmentTreeNode:
    __slots__ = ('l', 'r', 'lmx', 'rmx', 'mx', 'lc', 'rc', 'size', 'left', 'right')

    def __init__(self, l, r):
        self.l = l  # segment left index
        self.r = r  # segment right index
        self.lmx = self.rmx = self.mx = 0
        self.lc = self.rc = ''
        self.size = r - l + 1
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.root = None

    def build(self, s: str, l: int, r: int) -> SegmentTreeNode:
        node = SegmentTreeNode(l, r)
        if l == r:
            c = s[l]
            node.lmx = node.rmx = node.mx = 1
            node.lc = node.rc = c
            return node
        mid = (l + r) // 2
        node.left = self.build(s, l, mid)
        node.right = self.build(s, mid+1, r)
        return self.push_up(node)

    def push_up(self, node: SegmentTreeNode) -> SegmentTreeNode:
        left, right = node.left, node.right
        node.lc, node.rc = left.lc, right.rc
        node.size = left.size + right.size

        # prefix maximum
        node.lmx = left.lmx
        if left.lmx == left.size and left.rc == right.lc:
            node.lmx = left.size + right.lmx

        # suffix maximum
        node.rmx = right.rmx
        if right.rmx == right.size and left.rc == right.lc:
            node.rmx = right.size + left.rmx

        # overall maximum
        node.mx = max(left.mx, right.mx)
        if left.rc == right.lc:
            node.mx = max(node.mx, left.rmx + right.lmx)
        return node

    def update(self, node: SegmentTreeNode, idx: int, c: str):
        if node.l == node.r == idx:
            # leaf update
            node.lc = node.rc = c
            node.lmx = node.rmx = node.mx = 1
            return
        if idx <= node.left.r:
            self.update(node.left, idx, c)
        else:
            self.update(node.right, idx, c)
        self.push_up(node)

    def query_char(self, node: SegmentTreeNode, idx: int) -> str:
        if node.l == node.r == idx:
            return node.lc
        if idx <= node.left.r:
            return self.query_char(node.left, idx)
        else:
            return self.query_char(node.right, idx)

    def longestRepeating(self, s: str, queryCharacters: str, queryIndices: list[int]) -> list[int]:
        """
        Calculates the longest repeating character sequence after a series of updates.
        :param s: The initial string.
        :param queryCharacters: A string of characters to update.
        :param queryIndices: A list of indices corresponding to the characters in queryCharacters.
        :return: A list of integers, where each element is the length of the longest repeating
                 character sequence after the corresponding update.
        """

        n, m = len(s), len(queryCharacters)
        # init tree
        self.root = self.build(s, 0, n-1)
        res = []
        # process queries
        for c, idx in zip(queryCharacters, queryIndices):
            # if same char, result unchanged
            if self.query_char(self.root, idx) == c:
                res.append(self.root.mx)
                continue
            # update
            self.update(self.root, idx, c)
            res.append(self.root.mx)
        return res