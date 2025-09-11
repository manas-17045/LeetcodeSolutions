# Leetcode 1240: Tiling a Rectangle with ethe Fewest Squares
# https://leetcode.com/problems/tiling-a-rectangle-with-the-fewest-squares/
# Solved on 11th of September, 2025
import math


class Solution:
    def tilingRectangle(self, n: int, m: int) -> int:
        """
        Given a rectangle of size n x m, return the minimum number of square tiles to cover the whole rectangle.

        :param n: The height of the rectangle.
        :param m: The width of the rectangle.
        :return: The minimum number of square tiles.
        """
        # If square already
        if n == m:
            return 1

        # Ensure m is the larger dimension (width), keep n as height
        if n > m:
            n, m = m, n

        # Heights for each column (width m), initially 0
        heights = [0] * m
        ans = n * m

        # DFS using heights array
        def dfs(used: int):
            nonlocal ans

            # Prune if already worse or equal
            if used >= ans:
                return

            # If fully filled (all heights == n)
            if all(h == n for h in heights):
                ans = used
                return

            # Choose leftmost column with minimal height
            min_h = min(heights)
            i = heights.index(min_h)

            # Compute how many consecutive columns have this min height
            j = i
            while j < m and heights[j] == min_h:
                j += 1
            contiguous = j - i

            # Maximum square size we can place here
            max_s = min(n - min_h, contiguous)

            # Optional lower bound pruning by remaining area
            remaining_area = n * m - sum(heights)
            lower_bound = math.ceil(remaining_area / (n * n))
            if used + lower_bound >= ans:
                return

            # Try sizes from largest to smallest (greedy)
            for s in range(max_s, 0, -1):
                # Place square if size s at columns [i, i + s)
                for k in range(i, i + s):
                    heights[k] += s
                dfs(used + 1)
                # Backtrack
                for k in range(i, i + s):
                    heights[k] -= s

        dfs(0)
        return ans