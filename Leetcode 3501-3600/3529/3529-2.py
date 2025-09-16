# Leetcode 3529: Count Cells in Overlapping Horizontal and Vertical Substrings
# https://leetcode.com/problems/count-cells-in-overlapping-horizontal-and-vertical-substrings/
# Solved on 16th of September, 2025
class Solution:
    def countCells(self, grid: list[list[int]], pattern: str) -> int:
        """
        Counts the number of cells (r, c) in the grid such that the cell (r, c) is covered by at least one
        horizontal occurrence of the pattern and at least one vertical occurrence of the pattern.
        :param grid: A 2D list of integers representing the grid.
        :param pattern: A string representing the pattern to search for.
        :return: The total count of cells satisfying the condition.
        """
        m = len(grid)
        n = len(grid[0])
        N = m * n
        L = len(pattern)
        if L == 0:
            return 0

        # Build row-major text (concatenate rows left->right, top->bottom)
        row_parts = [''.join(grid[r]) for r in range(m)]
        row_text = ''.join(row_parts)

        # Build column-major text (concatenate columns top->bottom, left->right)
        col_parts = []
        for c in range(n):
            col_chars = [grid[r][c] for r in range(m)]
            col_parts.append(''.join(col_chars))
        col_text = ''.join(col_parts)

        # KMP prefix function
        def build_lps(pat: str) -> list[int]:
            l = len(pat)
            lps = [0] * l
            j = 0
            for i in range(1, l):
                while j > 0 and pat[i] != pat[j]:
                    j = lps[j - 1]
                if pat[i] == pat[j]:
                    j += 1
                    lps[i] = j
            return lps

        # KMP search: return start indices of matches in text
        def kmp_search(text: str, pat: str) -> list[int]:
            if len(pat) > len(text):
                return []
            lps = build_lps(pat)
            res = []
            i = 0
            j = 0
            T = len(text)
            P = len(pat)
            while i < T:
                if text[i] == pat[j]:
                    i += 1
                    j += 1
                    if j == P:
                        res.append(i - j)
                        j = lps[j - 1]
                else:
                    if j > 0:
                        j = lps[j - 1]
                    else:
                        i += 1
            return res

        # Find starts in row_text and col_text
        row_starts = kmp_search(row_text, pattern)
        col_starts = kmp_search(col_text, pattern)

        # Use difference arrays to mark coverage ranges in O(#starts)
        hor_diff = [0] * (N + 1)
        for s in row_starts:
            hor_diff[s] += 1
            hor_diff[s + L] -= 1

        vert_diff = [0] * (N + 1)
        for s in col_starts:
            vert_diff[s] += 1
            vert_diff[s + L] -= 1

        # Prefix sum to get coverage counts per linear index
        for i in range(1, N):
            hor_diff[i] += hor_diff[i - 1]
            vert_diff[i] += vert_diff[i - 1]

        # Count cells where both coverings are > 0
        cnt = 0
        for r in range(m):
            base_row = r * n
            for c in range(n):
                rIdx = base_row + c
                cIdx = c * m + r
                if hor_diff[rIdx] > 0 and vert_diff[cIdx] > 0:
                    cnt += 1

        return cnt