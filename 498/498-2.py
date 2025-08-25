# Leetcode 498: Diagonal Traverse
# https://leetcode.com/problems/diagonal-traverse/
# Solved on 25th of August, 2025
class Solution:
    def findDiagonalOrder(self, mat: list[list[int]]) -> list[int]:
        """
        Finds the diagonal order traversal of a given matrix.
        :param mat: The input matrix (list of lists of integers).
        :return: A list of integers representing the diagonal order traversal.
        """
        if not mat or not mat[0]:
            return []
        m, n = len(mat), len(mat[0])
        r = c = 0
        up = True  # direction: True => move up-right, False => move down-left
        res: list[int] = []
        total = m * n

        for _ in range(total):
            res.append(mat[r][c])
            if up:
                # Try moving up-right
                if c == n - 1:  # hit right border -> move down
                    r += 1
                    up = False
                elif r == 0:  # Hit top border -> move right
                    c += 1
                    up = False
                else:  # Normal move up-right
                    r -= 1
                    c += 1
            else:
                # Moving down-left
                if r == m - 1:  # hit bottom border -> move right
                    c += 1
                    up = True
                elif c == 0:  # hit left border -> move down
                    r += 1
                    up = True
                else:  # normal move down-left
                    r += 1
                    c -= 1

        return res